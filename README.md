# 🎵 Musiqa Qidiruvchi Telegram Bot

aiogram 3 va yt-dlp asosida qurilgan bot. Foydalanuvchi qo'shiq nomini yozadi,
bot YouTube'dan qidirib, tanlangan natijani audio (mp3) sifatida yuboradi.

## Tuzilma

```
music_bot/
├── main.py                 # Botni ishga tushirish
├── config.py               # .env dan tokenni o'qish
├── requirements.txt
├── .env.example
├── handlers/
│   ├── start.py            # /start komandasi
│   └── search.py           # qidirish va yuklab berish logikasi
├── services/
│   ├── music_search.py     # YouTube qidiruv
│   └── downloader.py        # audio yuklab olish
├── keyboards/
│   └── inline.py            # natijalar uchun tugmalar
└── utils/
    └── cleanup.py           # vaqtinchalik fayllarni tozalash
```

## O'rnatish

1. Python 3.10+ va **ffmpeg** o'rnatilgan bo'lishi kerak:
   ```bash
   sudo apt install ffmpeg
   ```

2. Kerakli kutubxonalarni o'rnating:
   ```bash
   pip install -r requirements.txt
   ```

3. `.env.example` faylini `.env` ga nomlang va tokenni kiriting:
   ```bash
   cp .env .env
   ```
   `.env` ichida:
   ```
   BOT_TOKEN=123456:ABC-DEF...
   ```
   Tokenni @BotFather orqali olasiz.

## Ishga tushirish

```bash
python main.py
```

## Qanday ishlaydi

1. Foydalanuvchi botga `/start` yuboradi.
2. Qo'shiq nomi yoki ijrochi+nom yoziladi (masalan: "Adele Hello").
3. Bot YouTube'dan 5 ta natija topib, tugmalar shaklida ko'rsatadi.
4. Foydalanuvchi tugmani bosadi → bot audio faylni yuklab, yuboradi.

## Eslatma

- Bu **Shazam emas** (audio orqali qo'shiq tanish), balki **matn bo'yicha
  musiqa qidirish va yuklash botidir** — chunki haqiqiy Shazam audio
  fingerprinting talab qiladi va bu ancha murakkab/qimmat.
- Mualliflik huquqi himoyalangan musiqani yuklab olish va tarqatish
  ba'zi mamlakatlarda cheklangan bo'lishi mumkin — botni shaxsiy/o'quv
  maqsadlarda ishlatish tavsiya etiladi.
