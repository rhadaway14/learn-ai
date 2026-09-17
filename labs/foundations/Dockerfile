FROM python:3.13-slim

WORKDIR /app
COPY api.py /app/api.py

RUN useradd --create-home --uid 10001 learner && mkdir -p /data && chown learner:learner /data
USER learner

EXPOSE 8080
CMD ["python", "/app/api.py"]
