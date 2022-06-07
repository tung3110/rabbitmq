

1. Cài đặt jenskin từ Dockerfile, chú ý trong Dockerfile phải có phần cài đặt docker tức là docker in docker để chạy các lệnh docker trong jenkins ( như file đính kèm)
    docker build -t jenkins_image:latest .
2. Chạy Dockêr
    docker run -d --name jenkins -p 8080:8080 -p 50000:50000 -v /var/run/docker.sock:/var/run/docker.sock -v jenkins_home:/var/jenkins_home jenkins_image:latest
