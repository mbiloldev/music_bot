import os
import yt_dlp

DOWNLOAD_DIR = "downloads"


def download_audio(video_id: str) -> str:
    """Berilgan video ID bo'yicha audio yuklab oladi va mp3 sifatida saqlaydi."""
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    url = f"https://www.youtube.com/watch?v={video_id}"
    output_template = os.path.join(DOWNLOAD_DIR, f"{video_id}.%(ext)s")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_template,
        "quiet": True,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return os.path.join(DOWNLOAD_DIR, f"{video_id}.mp3")
