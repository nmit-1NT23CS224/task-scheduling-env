<<<<<<< HEAD
FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

=======
FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

>>>>>>> 6fb65bbc529d4cc42624246fca08d99e8f1a4116
CMD ["python", "-u", "app.py"]