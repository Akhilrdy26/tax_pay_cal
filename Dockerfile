FROM ubuntu:latest

WORKDIR /app

COPY docker_flask /app/
COPY requirements.txt /app/

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    rm -rf /var/lib/apt/lists/*

RUN python3 -m venv venv1 && \
    /app/venv1/bin/pip install --upgrade pip && \
    /app/venv1/bin/pip install -r requirements.txt

CMD ["/bin/bash", "-c", "source /app/venv1/bin/activate && python3 /app/app.py"]
