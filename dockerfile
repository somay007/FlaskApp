FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install -r requirement.txt

EXPOSE 5000

CMD ["python", "app.py"]
