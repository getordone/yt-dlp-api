from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import subprocess
import os

app = FastAPI()

DOWNLOAD_PATH = "/app/downloads"
os.makedirs(DOWNLOAD_PATH, exist_ok=True)

@app.get("/download")
def download_video(url: str = Query(..., description="URL de la vidéo YouTube")):
    try:
        cmd = [
            "yt-dlp",
            "-f", "best",
            "-o", f"{DOWNLOAD_PATH}/%(title)s.%(ext)s",
            url
        ]
        subprocess.run(cmd, check=True)
        return JSONResponse(content={"status": "success", "message": "Video downloaded successfully"})
    except subprocess.CalledProcessError as e:
        return JSONResponse(status_code=500, content={"status": "error", "message": str(e)})
