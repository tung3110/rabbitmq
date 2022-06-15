from flask import Flask
import pika, sys, os
from threading import Timer,Thread,Event
Broker_local = "192.168.0.2"
app = Flask(__name__)
Vbat = "Battery: 12v"
@app.route("/")
def hello():
    return "Xin chào Nguyễn Huy Tùng"
@app.route("/api/hello")
def hello2():
    return "Xin Chao API by Docker Container 6888"
@app.route("/api/vbat")
def display():
    return Vbat
def rabbitmqConnect():
    global Vbat 
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=Broker_local))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        global Vbat
        print(" [x] Received %r" % body.decode())
        Vbat = body.decode()
        
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
class MyThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event
        
    def run(self):
        try:
            rabbitmqConnect()
        except KeyboardInterrupt:
            print('Interrupted')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
        
            
       
stopFlag = Event()
thread = MyThread(stopFlag)
thread.start()
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(debug=True,host='0.0.0.0',port=port)
    
    
    
