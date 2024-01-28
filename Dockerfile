FROM python:3.7

RUN mkdir /app
RUN mkdir /app/data
WORKDIR /app
ADD . /app/
ENV PYTHONUNBUFFERED=1
RUN pip install -r requirements.txt
# ARG GCP_SERVICE_ACCOUNT_KEY
# ENV GOOGLE_APPLICATION_CREDENTIALS=${GCP_SERVICE_ACCOUNT_KEY}
EXPOSE 5000
CMD ["python", "/app/hello.py"]