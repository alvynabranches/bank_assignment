FROM python:3.10

RUN python3 -m pip install --upgrade --no-cache-dir pip setuptools wheel
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000", "--reload" ]
