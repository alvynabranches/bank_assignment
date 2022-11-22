FROM python:3.11
RUN pip install --upgrade pip
RUN pip install kafka-python
RUN pip install pandas

WORKDIR /app
COPY consumer.py consumer.py
ENV CONTAINER true

CMD [ "python3", "consumer.py" ]