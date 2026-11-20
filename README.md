# Éclat Peau — Facial Skin Diagnosis & Skincare Recommendation System

Aplikasi web untuk mendiagnosis jenis kulit wajah dari foto dan memberikan rekomendasi bahan skincare yang sesuai, menggunakan Convolutional Neural Network (CNN).

Pengguna mengunggah atau mengambil foto wajah, lalu model CNN mengklasifikasikannya ke salah satu dari 4 jenis kulit — **normal, kering, berminyak, berjerawat** — dan menampilkan rekomendasi bahan perawatan kulit yang cocok. Aplikasi juga menyediakan halaman edukasi perawatan kulit, rekomendasi bahan, FAQ, dan berita perawatan kulit.

Proyek Capstone, Program Studi Teknik Informatika, Universitas Trisakti, 2024/2025.

## Teknologi

- **Model:** Convolutional Neural Network (CNN), MobileNetV2 sebagai base model + Softmax 4 kelas; training, testing, validasi, dan evaluasi (confusion matrix + accuracy) pada dataset dari Kaggle; augmentasi data (rotasi, flip, zoom, shear, brightness)
- **Backend:** Python, Flask, Gunicorn
- **Database:** MySQL (untuk login/register)
- **Frontend:** HTML, CSS, JavaScript

## Hasil model

Akurasi model naik dari **75%** (Oktober 2024) menjadi **92% pada data uji** (Januari 2025) melalui tuning hyperparameter, perluasan dataset, dan augmentasi data.

## Struktur folder

```text
.
├── run.py                  # Entry point Flask (port dari env PORT, fallback 8000)
├── config.py               # Konfigurasi (dibaca dari environment variable)
├── requirements.txt        # Dependensi Python (versi di-pin)
├── Procfile                # Perintah start untuk Railway/Heroku (gunicorn)
├── railway.json            # Konfigurasi deploy Railway (nixpacks)
├── .python-version         # Python 3.12 (TensorFlow 2.17 tidak mendukung 3.13)
├── init_db.sql             # Skema database MySQL (tabel users)
├── app/
│   ├── __init__.py         # App factory + koneksi MySQL
│   ├── routes.py           # Route: login, register, prediksi, edukasi, dll.
│   ├── database.py         # Helper koneksi database
│   ├── static/             # CSS, JS, gambar, dan folder uploads
│   └── templates/          # Template HTML
└── models/
    └── trained_model.keras # Model terlatih yang dipakai aplikasi (23 MB)
```

## Menjalankan secara lokal

```bash
# 1. Buat virtual environment dan install dependensi
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 2. Siapkan MySQL lokal (database `wajah_db`), lalu jalankan skemanya
mysql -u root wajah_db < init_db.sql

# 3. Jalankan aplikasi
python run.py
# Buka http://localhost:8000
```

Tanpa MySQL, aplikasi tetap bisa jalan, tetapi login/register akan gagal. Halaman prediksi (`/prediksi`) tidak membutuhkan database.

Environment variable yang didukung (opsional, ada fallback lokal):

| Variable | Default lokal |
|---|---|
| `SECRET_KEY` | nilai default di `config.py` / dibuat acak tiap start |
| `MYSQL_HOST` | `localhost` |
| `MYSQL_USER` | `root` |
| `MYSQL_PASSWORD` | (kosong) |
| `MYSQL_DB` | `wajah_db` |
| `PORT` | `8000` |

## Deploy ke Railway

1. Push repo ini ke GitHub.
2. Di Railway, buat project baru dari repo GitHub tersebut.
3. Tambahkan service **MySQL** ke project yang sama.
4. Di service web, isi environment variable berikut (ambil dari service MySQL):
   - `MYSQL_HOST` = `${{MySQL.MYSQLHOST}}`
   - `MYSQL_USER` = `${{MySQL.MYSQLUSER}}`
   - `MYSQL_PASSWORD` = `${{MySQL.MYSQLPASSWORD}}`
   - `MYSQL_DB` = `${{MySQL.MYSQLDATABASE}}`
   - `SECRET_KEY` = (isi string acak yang panjang)
5. Jalankan `init_db.sql` sekali di database MySQL Railway (mis. lewat Railway CLI atau MySQL client).
6. Deploy — Railway menjalankan `gunicorn run:app --workers 1 --timeout 300` (1 worker karena model TensorFlow berat; timeout panjang karena load model saat start butuh waktu).

## Catatan

- Folder `app/static/uploads/` sengaja dikosongkan dari repo: isinya foto-foto wajah yang di-upload saat testing. File upload pengguna baru akan tersimpan di sana saat aplikasi berjalan.
- Password pengguna disimpan tanpa hashing di database (sesuai kode asli proyek kuliah) — jangan dipakai apa adanya untuk production.
- Model dilatih di Google Colab; script training (`prediksi.py`) dan dataset tidak disertakan di repo ini.

## Tim

- **Sistem Cerdas:** Lulu Alfina Zahra, Affitra Nadine Dewi — training data, testing, validasi data, melatih model, evaluasi, preprocessing
- **Rekayasa Perangkat Lunak (RPL):** Aziza Ananta Endraswara, Dhevy Syahrilia Fadhila Putri
- Universitas Trisakti, 2024/2025
