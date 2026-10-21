# Virtual UV-Vis Laboratory

Prototipe tahap pertama aplikasi pembelajaran UV-Vis dengan model 3D interaktif yang terinspirasi dari bentuk luar Shimadzu UV-1800.

## Fitur tahap pertama
- Model 3D berbasis Three.js.
- Putar model menggunakan mouse.
- Zoom dengan scroll.
- Klik bagian model untuk membaca keterangan.
- Dibungkus dalam aplikasi Streamlit.

> Model merupakan ilustrasi edukasi, bukan replika teknis resmi. Geometri dan posisi komponen disederhanakan.

## Menjalankan secara lokal
Pastikan Python sudah terpasang. Dari folder proyek, jalankan:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Lalu buka URL lokal yang ditampilkan di terminal, biasanya `http://localhost:8501`.

## Struktur file
- `app.py` — aplikasi Streamlit dan model Three.js yang ditanamkan.
- `requirements.txt` — daftar dependensi Python.

## Deploy
Unggah file proyek ke repository GitHub, lalu buka Streamlit Community Cloud dan pilih `app.py` sebagai entrypoint.

Dokumentasi:
- https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app
- https://threejs.org/manual/

## Catatan
Three.js dimuat dari CDN, jadi koneksi internet diperlukan agar model 3D tampil.
