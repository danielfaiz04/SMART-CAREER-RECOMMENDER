# 📖 Manual Book - Smart Career Recommender

## Daftar Isi
1. [Pendahuluan](#pendahuluan)
2. [Persyaratan Sistem](#persyaratan-sistem)
3. [Instalasi dan Setup](#instalasi-dan-setup)
4. [Panduan Penggunaan](#panduan-penggunaan)
5. [Fitur-Fitur Utama](#fitur-fitur-utama)
6. [Troubleshooting](#troubleshooting)
7. [FAQ](#faq)
8. [Kontak dan Dukungan](#kontak-dan-dukungan)

---

## Pendahuluan

**Smart Career Recommender** adalah aplikasi web cerdas yang membantu pengguna menemukan rekomendasi karir yang sesuai berdasarkan minat, skill, pengalaman, dan kepribadian mereka. Aplikasi ini menggunakan kombinasi Machine Learning (Decision Tree Classifier) dan Rule-Based Engine untuk memberikan rekomendasi yang akurat.

### Tujuan Aplikasi
- Membantu individu menemukan karir yang sesuai dengan profil mereka
- Memberikan roadmap pembelajaran untuk mengembangkan skill
- Menyediakan informasi detail tentang berbagai profesi
- Menyimpan riwayat rekomendasi untuk tracking perkembangan

### Teknologi yang Digunakan
- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python Flask
- **Machine Learning**: Scikit-learn (Decision Tree Classifier)
- **Database**: JSON files untuk penyimpanan data
- **AI Integration**: Google Gemini API untuk fitur chat

---

## Persyaratan Sistem

### Minimum Requirements
- **Operating System**: Windows 10/11, macOS 10.15+, Linux Ubuntu 18.04+
- **RAM**: 4GB
- **Storage**: 500MB free space
- **Browser**: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+

### Software Requirements
- **Python**: 3.8 atau lebih baru
- **Git**: Untuk cloning repository (opsional)
- **Web Browser**: Dengan JavaScript enabled

### Dependencies Python
```
Flask==2.3.3
Flask-CORS==4.0.0
scikit-learn==1.3.2
numpy==1.24.3
requests==2.31.0
google-generativeai>=0.3.0
python-dotenv>=1.0.0
```

---

## Instalasi dan Setup

### Langkah 1: Download Project
```bash
# Clone dari GitHub (jika tersedia)
git clone https://github.com/username/smart-career-recommender.git
cd smart-career-recommender

# Atau download ZIP dan extract
```

### Langkah 2: Setup Environment
```bash
# Buat virtual environment
python -m venv venv

# Aktivasi virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Langkah 3: Konfigurasi Environment Variables
```bash
# Copy file environment example
cp backend/.env.example backend/.env

# Edit file .env dan isi API key jika diperlukan
# GEMINI_API_KEY=your_api_key_here
```

### Langkah 4: Jalankan Aplikasi
```bash
# Dari root directory project
python app.py

# Aplikasi akan berjalan di: http://127.0.0.1:5000
```

### Langkah 5: Akses Aplikasi
Buka browser dan kunjungi: `http://127.0.0.1:5000`

---

## Panduan Penggunaan

### Halaman Utama (Form Input)

1. **Pilih Minat Anda**
   - Pilih dari 5 kategori: Desain, Marketing, Administrasi, Teknologi, Penjualan
   - Pilihan ini akan mempengaruhi rekomendasi karir

2. **Pilih Skill yang Dimiliki**
   - Centang semua skill yang Anda kuasai
   - Skill akan dimuat otomatis dari sistem
   - Minimal pilih 1 skill, maksimal tidak terbatas

3. **Pilih Tingkat Pengalaman**
   - **Pemula**: < 1 tahun pengalaman
   - **Menengah**: 1-5 tahun pengalaman
   - **Senior**: > 5 tahun pengalaman

4. **Pilih Tipe Kepribadian**
   - **Introvert**: Lebih suka bekerja sendiri
   - **Ambivert**: Kombinasi introvert dan extrovert
   - **Extrovert**: Lebih suka interaksi sosial

5. **Submit Form**
   - Klik tombol "Dapatkan Rekomendasi"
   - Sistem akan memproses dan menampilkan hasil

### Halaman Hasil Rekomendasi

1. **Top 3 Rekomendasi Karir**
   - Menampilkan 3 posisi karir teratas
   - Setiap rekomendasi memiliki skor kecocokan (0-100%)

2. **Detail Setiap Rekomendasi**
   - **Deskripsi Pekerjaan**: Penjelasan singkat tentang posisi
   - **Skill yang Dibutuhkan**: Skill yang harus dikuasai
   - **Skill yang Perlu Dipelajari**: Skill tambahan untuk dikembangkan
   - **Roadmap Pembelajaran**: Panduan step-by-step

3. **Aksi yang Tersedia**
   - **Lihat Detail**: Informasi lebih lengkap tentang karir
   - **Tanya AI**: Konsultasi dengan AI tentang karir tersebut
   - **Export PDF**: Simpan rekomendasi dalam format PDF

---

## Fitur-Fitur Utama

### 1. Sistem Rekomendasi Cerdas 🤖
- **Machine Learning Model**: Decision Tree Classifier yang dilatih dari dataset
- **Rule-Based Engine**: Aturan logis yang menggabungkan multiple faktor
- **Preprocessing**: One-Hot Encoding dan Multi-Label Binarization

### 2. Chat dengan AI 💬
- Konsultasi langsung dengan AI tentang karir pilihan
- Tanyakan detail pekerjaan, prospek karir, gaji, dll.
- Didukung oleh Google Gemini API

### 3. Detail Informasi Karir 📋
- Deskripsi lengkap setiap posisi
- Persyaratan skill dan pengalaman
- Prospek karir dan perkembangan
- Estimasi gaji (berdasarkan data umum)

### 4. Riwayat Rekomendasi 📊
- Simpan semua hasil rekomendasi
- Lihat 50 prediksi terakhir
- Tracking perkembangan karir Anda

### 5. Export dan Sharing 📄
- Export rekomendasi ke format PDF
- Bagikan hasil dengan mudah
- Simpan untuk referensi di masa depan

### 6. Responsive Design 📱
- Kompatibel dengan desktop dan mobile
- Interface yang user-friendly
- Dark/Light mode support

---

## Troubleshooting

### Masalah: Aplikasi Tidak Bisa Dijalankan
**Solusi:**
1. Pastikan Python 3.8+ terinstall
2. Aktivasi virtual environment: `venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Jalankan: `python app.py`

### Masalah: Port 5000 Sudah Digunakan
**Solusi:**
```bash
# Gunakan port berbeda
python app.py --port 8000
# Atau kill process yang menggunakan port 5000
```

### Masalah: Model Tidak Dapat Dimuat
**Solusi:**
1. Pastikan file `backend/model.pkl` ada
2. Pastikan versi scikit-learn kompatibel
3. Reinstall dependencies jika perlu

### Masalah: Browser Tidak Dapat Mengakses
**Solusi:**
1. Pastikan aplikasi berjalan (lihat terminal output)
2. Coba URL alternatif:
   - `http://127.0.0.1:5000`
   - `http://localhost:5000`
3. Disable firewall sementara untuk testing

### Masalah: Fitur Chat AI Tidak Berfungsi
**Solusi:**
1. Pastikan `GEMINI_API_KEY` sudah diisi di file `.env`
2. Periksa koneksi internet
3. API key valid dan memiliki quota

---

## FAQ

### Q: Apakah aplikasi ini gratis?
A: Ya, aplikasi ini open source dan gratis untuk digunakan.

### Q: Berapa akurasi rekomendasi karir?
A: Akurasi bervariasi tergantung input pengguna, namun sistem menggunakan kombinasi ML dan rule-based untuk hasil optimal.

### Q: Apakah data saya disimpan?
A: Data rekomendasi disimpan secara lokal di file JSON untuk riwayat. Tidak ada data yang dikirim ke server eksternal kecuali untuk fitur chat AI.

### Q: Bagaimana cara mengupdate model ML?
A: Jalankan script `ml/train_model.py` dengan dataset baru, lalu replace file `model.pkl`.

### Q: Apakah bisa digunakan offline?
A: Ya, semua fitur kecuali chat AI bisa digunakan offline. Chat AI memerlukan koneksi internet.

### Q: Bagaimana cara backup data?
A: Copy file `backend/history.json` untuk backup riwayat rekomendasi.

### Q: Apakah support bahasa Indonesia?
A: Ya, interface dan output dalam bahasa Indonesia.

---

## Kontak dan Dukungan

### Developer
- **Nama**: [Nama Developer]
- **Email**: [Email Developer]
- **GitHub**: [GitHub Repository]

### Cara Mendapatkan Bantuan
1. **Documentation**: Baca manual ini secara lengkap
2. **GitHub Issues**: Laporkan bug atau request fitur
3. **Forum Komunitas**: Diskusi dengan pengguna lain

### Update dan Maintenance
- Aplikasi akan diupdate secara berkala
- Ikuti repository GitHub untuk update terbaru
- Backup data penting sebelum update

---

## Lisensi

Aplikasi ini menggunakan lisensi MIT. Silakan lihat file LICENSE untuk detail lebih lanjut.

---

*Manual Book ini dibuat untuk membantu pengguna memahami dan menggunakan Smart Career Recommender dengan optimal. Untuk pertanyaan lebih lanjut, silakan hubungi developer.*