# Smart Career Recommender 💼

Aplikasi sistem cerdas yang memberikan rekomendasi pekerjaan dan skill berdasarkan input pengguna menggunakan Machine Learning dan Rule-Based Engine.

## Fitur Utama

✨ **User Input Form**
- Pilih minat (desain, marketing, administrasi, teknologi, penjualan)
- Centang skill yang dimiliki
- Pilih tingkat pengalaman (pemula, menengah, senior)
- Tentukan tipe kepribadian (introvert, ambivert, extrovert)

🤖 **Machine Learning Model**
- Decision Tree Classifier untuk prediksi karir
- Dilatih dari 25 dataset samples
- Preprocessing dengan One-Hot Encoding dan Multi-Label Binarization

📋 **Rule-Based Engine**
- Aturan logis yang menggabungkan kepribadian, minat, dan skill
- Meningkatkan akurasi prediksi dengan business rules

📊 **Output Rekomendasi**
- Top 3 rekomendasi pekerjaan
- Skor kecocokan (0-100%)
- Skill yang perlu dipelajari
- Roadmap pembelajaran singkat

💾 **Riwayat Prediksi**
- Menyimpan semua prediksi ke file JSON
- Dapat melihat 50 prediksi terakhir

## Struktur Folder

```
smart-career-recommender/
├── frontend/
│   ├── index.html          # Halaman input form
│   ├── result.html         # Halaman hasil rekomendasi
│   └── style.css           # Styling semua halaman
├── backend/
│   ├── app.py              # Flask server & endpoints
│   ├── dataset.json        # Training dataset (25 samples)
│   ├── model.pkl           # Model ML yang sudah dilatih
│   └── history.json        # Riwayat prediksi
├── ml/
│   └── train_model.py      # Script untuk melatih model
├── requirements.txt        # Python dependencies
└── README.md              # File ini
```

## Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python Flask
- **Machine Learning**: scikit-learn (Decision Tree Classifier)
- **Database**: JSON (static)
- **API**: RESTful dengan JSON

## Installation & Setup

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Training ML Model

```bash
cd ml
python train_model.py
```

Output:
- `backend/model.pkl` (model yang sudah dilatih)

### 3. Run Backend Server

```bash
cd backend
python app.py
```

Server akan berjalan di `http://localhost:5000`

### 4. Akses Frontend

Buka file `frontend/index.html` di browser atau gunakan live server:

```bash
# Jika menggunakan Python
cd frontend
python -m http.server 8000
```

Akses di `http://localhost:8000/index.html`

## API Endpoints

### POST /predict

Mendapatkan rekomendasi pekerjaan berdasarkan input user.

**Request:**
```json
{
  "interest": "teknologi",
  "skills": ["programming", "database"],
  "experience": "menengah",
  "personality": "introvert"
}
```

**Response:**
```json
{
  "success": true,
  "jobs": [
    {
      "title": "Backend Developer",
      "score": 87,
      "skills_to_learn": ["API development", "DevOps"],
      "roadmap": "Python/JavaScript fundamentals → Database design → API development → DevOps"
    },
    {
      "title": "Data Analyst",
      "score": 82,
      "skills_to_learn": ["SQL", "Data visualization"],
      "roadmap": "SQL → Python → Data visualization → Statistical analysis"
    },
    {
      "title": "IT Support Specialist",
      "score": 75,
      "skills_to_learn": ["Networking", "Troubleshooting"],
      "roadmap": "Networking basics → Troubleshooting → Hardware knowledge → Ticketing systems"
    }
  ]
}
```

### GET /history

Mendapatkan riwayat semua prediksi yang telah dilakukan.

**Response:**
```json
{
  "success": true,
  "history": [
    {
      "interest": "teknologi",
      "skills": ["programming"],
      "experience": "menengah",
      "personality": "introvert",
      "timestamp": "2025-11-27T10:30:45.123456",
      "results": [...]
    }
  ]
}
```

### GET /api/options

Mendapatkan daftar option yang tersedia untuk form.

**Response:**
```json
{
  "success": true,
  "interests": ["administrasi", "desain", "marketing", "penjualan", "teknologi"],
  "experiences": ["menengah", "pemula", "senior"],
  "personalities": ["introvert", "ambivert", "extrovert"],
  "skills": ["adobe", "analytics", "api", ...]
}
```

## Dataset Struktur

File `backend/dataset.json` berisi 25 training samples dengan format:

```json
{
  "interest": "desain",
  "skills": ["canva", "editing"],
  "experience": "pemula",
  "personality": "introvert",
  "job": "Graphic Designer"
}
```

**Fields:**
- `interest`: kategori minat (5 pilihan)
- `skills`: array skill yang dimiliki (multi-label)
- `experience`: tingkat pengalaman (3 pilihan)
- `personality`: tipe kepribadian (3 pilihan)
- `job`: pekerjaan yang direkomendasikan

## ML Model Details

### Preprocessing
1. **Interest**: One-Hot Encoding (5 kategori)
2. **Experience**: Label Encoding (3 kategori)
3. **Personality**: Label Encoding (3 kategori)
4. **Skills**: Multi-Label Binarization (dinamis)

### Algorithm
- **Decision Tree Classifier**
  - Max depth: 5
  - Untuk mencegah overfitting
  - Simple dan interpretable

### Features
- Total features: ~20-25 (tergantung jumlah unique skills)
- Training samples: 25
- Target classes: 25 jenis pekerjaan

## Rule-Based Engine

Aturan logis yang diterapkan:

1. **Introvert + Design** → Graphic Designer, UI/UX Designer, Video Editor
2. **Extrovert + Marketing** → Digital Marketing, PPC Specialist
3. **Extrovert + Sales** → Sales Executive, Account Executive, Business Development Manager
4. **Admin Skills + Office** → Admin Officer, Office Manager, Project Coordinator
5. **Tech Skills + Technology** → Backend Developer, Data Analyst, IT Support, DevOps Engineer
6. **Data Entry + Beginner** → Data Entry Operator
7. **Frontend Skills** → Frontend Developer, Web Designer
8. **Content + Marketing** → Content Creator
9. **Ambivert + Marketing** → SEO Specialist, Marketing Automation Specialist, Content Creator

## Skill Recommendations

Untuk setiap pekerjaan, aplikasi menyediakan:
1. **Skills to Learn**: Top 3 skill yang perlu dipelajari user
2. **Roadmap**: Jalur pembelajaran terstruktur

Contoh untuk Backend Developer:
> "Python/JavaScript fundamentals → Database design → API development → DevOps"

## User Interface

### Halaman Input (index.html)
- Form dengan 4 field input
- Clean dan modern design
- Responsive untuk mobile

### Halaman Hasil (result.html)
- Kartu hasil dengan score persentase
- Skill yang perlu dipelajari
- Roadmap pembelajaran
- Tombol untuk mencoba ulang

### Styling
- Gradient background (purple-blue)
- Card-based layout
- Smooth animations
- Mobile responsive

## Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Troubleshooting

### Error: "Terjadi kesalahan. Pastikan server berjalan!"
- Pastikan backend server berjalan: `python app.py`
- Pastikan running di port 5000
- Check CORS headers

### Model tidak ditemukan
```bash
cd ml
python train_model.py
```

### Port 5000 sudah terpakai
Edit `app.py` baris terakhir:
```python
app.run(debug=True, port=5001)  # Ubah ke port lain
```

## Development

### Menambah Pekerjaan Baru
1. Tambahkan data ke `backend/dataset.json`
2. Update `skill_roadmaps` dan `job_skills_required` di `backend/app.py`
3. Re-train model: `python ml/train_model.py`

### Menambah Rule Baru
Edit function `get_rule_based_recommendations()` di `backend/app.py`

### Menambah Skill Baru
Cukup tambahkan skill ke dataset, akan otomatis terdeteksi.

## Future Enhancements

- [ ] Database dengan SQLite/PostgreSQL
- [ ] User authentication
- [ ] Career progression tracking
- [ ] Skill gap analysis lebih detail
- [ ] Integration dengan job portals
- [ ] API documentation dengan Swagger
- [ ] Unit tests dan integration tests
- [ ] Docker containerization

## Performance

- **Model Training**: ~0.1 detik
- **Prediction**: ~10-50ms
- **API Response**: ~50-100ms
- **Frontend Load**: ~500ms

## License

MIT License - Bebas digunakan untuk keperluan apapun

## Author

Smart Career Recommender v1.0 - 2025

## Support

Untuk pertanyaan atau bug report, silakan buat issue di repository ini.

---

**Happy Career Hunting! 🚀**
