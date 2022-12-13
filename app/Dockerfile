FROM python:3.11

RUN pip install --upgrade pip setuptools wheel
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000
COPY . .

CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000", "--reload", "--workers", "4" ]