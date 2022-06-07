1. Caì đặt nginx từ dockerfile
	docker build -t nginx-jenkins .
2. Chay docker tu image
	docker run -d -p 80:80 -p 443:443 nginx-jenkins:latest
2. Cấu hình HTTPS cho site api và site jenkins manager
	sudo apt update && sudo apt install certbot python3-certbot-nginx
	sudo certbot --nginx
