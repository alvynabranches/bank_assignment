FROM python:3.10
RUN pip install --upgrade pip
RUN pip install kafka-python
RUN pip install pytz

WORKDIR /app
COPY producer.py producer.py
ENV CONTAINER true

CMD [ "python3", "producer.py" ]