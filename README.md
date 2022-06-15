1. Cài MQTT,Rabbitmq ở localhost có địa chỉ IP local là 192.168.0.2
2. Chạy file server.py ở máy áo ubuntu. chương trình này có nhiệm vụ nhận lệnh MQTT và publish cho rabbitmq 
3. Build và chạy chương trình app.py tại docker ở localhost, chương trình này có nhiệm vụ 
	- nhận lệnh subcrible từ Rabbitmq
	- đẩy lên web thông qua cổng HTTP cổng 80
	- dùng ngrok để lấy public lên web
	- dùng EC2 cấu hình nginx tại địa chỉ vbat.hoalancaycanh.com.vn
4.