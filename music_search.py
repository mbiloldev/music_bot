import yt_dlp


def search_music(query: str, limit: int = 5) -> list[dict]:
    """Berilgan so'rov bo'yicha YouTube'dan qo'shiqlarni qidiradi."""
    ydl_opts = {
        "quiet": True,
        "extract_flat": True,
        "skip_download": True,
        "default_search": f"ytsearch{limit}",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=False)

    results = []
    for entry in info.get("entries", []):
        results.append({
            "id": entry["id"],
            "title": entry.get("title", "Noma'lum"),
            "duration": entry.get("duration") or 0,
        })
    return results
