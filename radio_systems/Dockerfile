FROM ubuntu:22.04
RUN apt-get update && \
    apt-get install -y wget python3  python3-pip && \
    apt-get clean

COPY search_path.sh extract_path_value.py config.txt /tmp/

RUN chmod +x /tmp/search_path.sh /tmp/extract_path_value.py

# docker build -t extractor .
# docker run --name extractor extractor