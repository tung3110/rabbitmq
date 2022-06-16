import paho.mqtt.client as mqtt #import the client1
import time
import ssl
import pika
import json
Broker_local =  "192.168.0.3"
try:
  connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=Broker_local))
  channel = connection.channel()

  channel.queue_declare(queue='hello')

  channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
  print(" [x] Sent 'Hello World!'")
  connection.close()
except:
   print("Khong the ket noi Rabbitmq host: " + Broker_local)
def rabbitmq_send(dataSend):
  connection = pika.BlockingConnection(pika.ConnectionParameters(host=Broker_local))
  channel = connection.channel()
  channel.queue_declare(queue='hello')
  channel.basic_publish(exchange='', routing_key='hello', body=dataSend)
  connection.close()
############
def on_message_local(client2, userdata, msg):
   #global PlayVlc,MQTT_Timeout,MQTT_Flag,MountPoint,LocalMaster
   #MQTT_Timeout = 40
   #MQTT_Flag = 1
   message = str(msg.payload.decode("utf-8"))
   print("MQTT Local " + msg.topic  + ":  " + message)
   try:
      #s1 = json.dumps(message)
      #print(s1)
      vbat = json.loads(message)["battery"]
      print("Điệp áp:"+ str(vbat))
      if(vbat<10):
         rabbitmq_send("Cảnh báo điệp áp thấp, điệp áp: "+str(vbat)+" v")
      else:
         rabbitmq_send("Điệp áp: "+str(vbat) + " v")
   except:
      print("Json không đúng định dạng")
def on_connect_local(client2, userdata, flags, rc):
   #global MountPoint,MQTT_Flag_Local
   print("Connected Host Local  with result code " + str(rc))
   #client2.subscribe("vs/sub/{}".format("amzMaster"))
   client2.subscribe("develops/data")
   print("Subcriibe topic develops/data")
   #publish_mqtt_local("vs/pub/{}".format("amzMaster"),"TEST MQTT ")
def publish_mqtt_local(topic,sensor_data):
   global MountPoint
   try:
       mqttc = mqtt.Client("python_pub")
       mqttc.connect(Broker_local, 1883)
       mqttc.publish(topic, sensor_data)
       print("publish topic: {}, msg: {}".format(topic,sensor_data))
   except:
       print("Can not connect local")
   #mqttc.loop(2) //timeout = 2s
def ConectMQTT_Local():

#        try:
                print("Ket noi local {}".format(Broker_local))
                #global MQTT_Timeout
                #MQTT_Timeout = 30
                client2 = mqtt.Client()
                client2.on_connect = on_connect_local
                client2.on_message = on_message_local
                client2.tls_set(ca_certs="ca-cert.pem", certfile="client-cert.pem", keyfile="client-key.pem",tls_version=ssl.PROTOCOL_TLSv1_2)
                client2.tls_insecure_set(True)
                client2.connect(Broker_local, 8883, 60)
                client2.loop_start()
 #       except:
                #MQTT_Flag = 0
  #              print("Khong the ket noi local")
ConectMQTT_Local()
def on_publish_local(mosq, obj, mid):
   print("mid: " + str(mid))
time.sleep(4) # wait
while True:
    time.sleep(1)
#client2.loop_stop() #stop the loop