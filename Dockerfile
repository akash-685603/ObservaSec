FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdir -p /var/log/observasec && chown -R 65532:65532 /var/log/observasec
EXPOSE 5000
USER 65532
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers", "2"]
