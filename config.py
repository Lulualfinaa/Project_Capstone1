import os


class Config:
    # SECRET_KEY dibaca dari environment variable bila ada (mis. di Railway),
    # bila tidak ada dipakai nilai lokal ini (jangan dipakai di production).
    SECRET_KEY = os.getenv(
        'SECRET_KEY',
        '5e4c3d2b1a0f9e8c7b6a5d4c3e2f1a0b0f9e8c7d6b5a4bg43'
    )
    # Kredensial MySQL: dibaca dari environment variable bila ada,
    # fallback ke konfigurasi lokal (localhost / root / tanpa password).
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
    MYSQL_DB = os.getenv('MYSQL_DB', 'wajah_db')
