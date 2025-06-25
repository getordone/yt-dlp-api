FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y ffmpeg curl && \
    pip install fastapi uvicorn yt-dlp

WORKDIR /app
COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
