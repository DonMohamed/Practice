FROM python:alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN  pip3 install --no-cache-dir -r requirments.txt

EXPOSE 8080

CMD ["python3", "toDoList.py"]
        