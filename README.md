1. Cài đặt rbbitmq : 
	sudo docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.10-management
3. Cài MQTT,Rabbitmq ở máy ảo ubuntu
4. Chạy file vbatssl.py ở máy áo ubuntu. chương trình này có nhiệm vụ nhận lệnh MQTT và publish cho rabbitmq 
5. Build và chạy chương trình app.py tại docker ở localhost, chương trình này có nhiệm vụ 
	- nhận lệnh subcrible từ Rabbitmq
	- đẩy lên web thông qua cổng HTTP cổng 80
	- dùng ngrok để lấy public lên web
	- dùng EC2 cấu hình nginx tại địa chỉ vbat.hoalancaycanh.com.vn
6.
