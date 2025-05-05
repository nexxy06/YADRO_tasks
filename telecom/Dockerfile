FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* 

WORKDIR /app

COPY requirements.txt .
COPY checkHTTP.py .

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

CMD [ "python3", "checkHTTP.py" ]

# docker build -t http-checker .
# docker run http-checker