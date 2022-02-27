FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./

RUN apt-get update && \
    apt-get install nano && apt-get clean all && \
    pip install --no-cache-dir -r requirements.txt

ENV PORT=8080

EXPOSE 8080

COPY . .

CMD [ "python", "server.py" ]