FROM python:3

WORKDIR /opt/ddns

RUN pip install boto3 requests

COPY . .

ENTRYPOINT ["python", "./main.py"]