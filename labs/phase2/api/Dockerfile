FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY labs/phase2/api/requirements.txt /app/requirements.txt
RUN python -m pip install --no-cache-dir -r /app/requirements.txt \
    && python -m pip install --no-cache-dir "torch>=2.4,<3" --index-url https://download.pytorch.org/whl/cpu \
    && useradd --create-home --uid 10001 learner \
    && mkdir -p /artifacts/phase2 \
    && chown -R learner:learner /artifacts

COPY labs/__init__.py /app/labs/__init__.py
COPY labs/phase2/__init__.py /app/labs/phase2/__init__.py
COPY labs/phase2/api /app/labs/phase2/api

USER learner
EXPOSE 8080
CMD ["python", "-m", "uvicorn", "labs.phase2.api.main:app", "--host", "0.0.0.0", "--port", "8080"]
