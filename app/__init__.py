from flask import Flask
from .routes import main
from .database import close_db
from mysql.connector import connect, Error
import mysql.connector
import os

def create_app():
    app = Flask(__name__)

    # Konfigurasi koneksi MySQL: dibaca dari environment variable bila ada
    # (mis. di Railway), fallback ke konfigurasi lokal bila tidak ada.
    # Tanpa MySQL, aplikasi tetap jalan; hanya login/register yang gagal.
    app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'localhost')
    app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')
    app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', '')
    app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'wajah_db')

    # Inisialisasi koneksi MySQL
    app.db_connection = create_db(app)

     # Konfigurasi untuk folder upload
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/uploads')
    app.register_blueprint(main)

    @app.teardown_appcontext
    def teardown_db(exception):
        close_db(app.db_connection)

    return app

def create_db(app):
    # Inisialisasi MySQL (menggunakan mysql-connector)

    try:
        connection = mysql.connector.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            database=app.config['MYSQL_DB']
        )
        print("Koneksi ke MySQL berhasil!")
    except Error as e:
        print(f"Error saat menghubungkan ke MySQL: {e}")
        connection = None

    return connection
