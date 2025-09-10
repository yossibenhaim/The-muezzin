FROM python:3.12-slim AS builder

WORKDIR /speach_to_text

COPY . /speach_to_text

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD ["sh", "-c", "python -m speach_to_text.kafka_stt.sub-stt"]
