FROM python:3.12-slim AS builder

WORKDIR /information_analysis

COPY . /information_analysis

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD ["sh", "-c", "python -m information_analysis.kafka_analysis.sub-analysis"]
