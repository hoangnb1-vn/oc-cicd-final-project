FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 8080
USER 1001
CMD ["python", "app.py"]
