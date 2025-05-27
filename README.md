## 💻 ML_Face_Recognition
Sistem face recognition berbasis Machine Learning menggunakan dataset yang diambil secara langsung melalui kamera. Proyek ini memanfaatkan **OpenCV** untuk perekaman wajah, pelatihan model, dan pengenalan wajah.

## ⚙️ Persiapan

Pastikan Anda telah menginstal dependensi berikut sebelum menjalankan program:

```bash
pip install opencv-python
```

## 🚀 Langkah Penggunaan

### 1. Rekam Wajah

Untuk merekam wajah dan menyimpan dataset:

```bash
python rekam.py
```

* Masukkan **ID** saat diminta.
* Gambar wajah akan disimpan otomatis di folder `./dataset/`.

### 2. Training Dataset

Untuk melatih model pengenalan wajah menggunakan data yang telah direkam:

```bash
python training.py
```

* Model hasil training akan disimpan secara otomatis.

### 3. Pengenalan Wajah

Untuk memulai proses deteksi dan pengenalan wajah secara real-time:

```bash
python scan.py
