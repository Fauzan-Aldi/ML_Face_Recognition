Berikut versi yang lebih **teknis, rapi, dan profesional** dari deskripsi tersebut:

---

# 💻 Machine Learning Face Recognition 📷

![Preview](https://user-images.githubusercontent.com/48589121/200715958-b3988afd-fa22-40e9-8c9e-3b60cff442a9.png)

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
```

* Program akan mencocokkan wajah yang terdeteksi dengan data yang telah dilatih sebelumnya.

---

Ingin saya bantu juga membuatkan file `README.md` atau struktur folder proyek ini?
