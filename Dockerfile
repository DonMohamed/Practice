FROM python:alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN  pip3 install --no-cache-dir -r requirements.txt \
     && addgroup -S app && adduser -S app -G app \
     && chown -R app:app . 

EXPOSE 8080
USER app

CMD ["python3", "toDoList.py"]
        