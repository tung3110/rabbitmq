FROM python:latest
MAINTAINER Tungnh "nguyenhuytung@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
EXPOSE 80