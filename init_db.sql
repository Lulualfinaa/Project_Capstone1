-- Skema database Éclat Peau.
-- Jalankan file ini sekali di database MySQL yang dipakai aplikasi
-- (lokal: database `wajah_db`; di Railway: database MySQL service,
-- nama databasenya sesuaikan dengan environment variable MYSQL_DB).
-- Satu-satunya tabel yang dipakai aplikasi adalah `users`
-- (dipakai route login dan register di app/routes.py).

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
