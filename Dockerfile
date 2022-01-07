FROM python:3.9

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python3", "main.py"]