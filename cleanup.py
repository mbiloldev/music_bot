import os
import shutil


def clean_downloads(path: str = "downloads") -> None:
    """Yuklab olingan fayllar papkasini tozalaydi (bot ishga tushganda)."""
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path, exist_ok=True)
