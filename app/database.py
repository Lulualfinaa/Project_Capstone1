import mysql.connector
from flask import current_app, g

# Skema tabel users (sama persis dengan init_db.sql).
# Dibuat otomatis setiap kali koneksi DB berhasil, supaya login/register
# langsung jalan tanpa menjalankan init_db.sql secara manual di server.
CREATE_USERS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
"""

def ensure_users_table(connection):
    """Buat tabel users bila belum ada. Idempotent; gagal dengan aman
    (hanya mencetak error, tidak pernah melempar exception)."""
    try:
        cursor = connection.cursor()
        cursor.execute(CREATE_USERS_TABLE_SQL)
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Tidak bisa membuat tabel users: {e}")

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=current_app.config['MYSQL_HOST'],
            user=current_app.config['MYSQL_USER'],
            password=current_app.config['MYSQL_PASSWORD'],
            database=current_app.config['MYSQL_DB']
        )
        ensure_users_table(g.db)
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
