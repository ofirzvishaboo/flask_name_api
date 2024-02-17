FROM python:3.9-slim
LABEL authors="ofirzvishaboo"

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY User_Creation_API .

EXPOSE 3000
ENV database_host mysql-service

CMD ["python", "rest_app.py"]
