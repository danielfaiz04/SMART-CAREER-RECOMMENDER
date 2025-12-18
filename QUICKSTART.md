# 🚀 QUICK START GUIDE

## Cara Menjalankan Smart Career Recommender

### Requirement
- Python 3.9+
- pip (Python package manager)

### Step 1: Install Dependencies

```bash
cd "c:\laragon\www\Smart Career Recommender"
pip install -r requirements.txt
```

Atau jika menggunakan virtual environment:

```bash
# Create venv (jika belum ada)
python -m venv .venv

# Activate venv
.\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Train Machine Learning Model

Hanya perlu dilakukan sekali saat setup pertama:

```bash
cd ml
python train_model.py
```

Output: `backend/model.pkl` akan dibuat

### Step 3: Run Backend Server

**Terminal 1 - Backend Server:**
```bash
cd backend
python -m flask run --host=0.0.0.0 --port=5000
```

Atau menggunakan python langsung:
```bash
cd backend
python app.py
```

Server akan berjalan di: `http://localhost:5000`

### Step 4: Open Frontend

**Terminal 2 - Frontend (atau buka langsung):**

Opsi 1: Buka langsung di browser
```
c:\laragon\www\Smart Career Recommender\frontend\index.html
```

Opsi 2: Gunakan Python HTTP Server
```bash
cd frontend
python -m http.server 8000
```

Buka di browser: `http://localhost:8000/index.html`

Opsi 3: Gunakan Laragon (jika sudah setup)
- Akses via Laragon virtual host

---

## 🧪 Testing API

### Test Endpoints dengan Python

```bash
python test_api.py
```

### Test di Browser

Buka file `frontend/test.html` untuk interactive API testing

### Test dengan curl

```bash
# Test GET /api/options
curl http://localhost:5000/api/options

# Test POST /predict
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d "{\"interest\":\"teknologi\",\"skills\":[\"programming\"],\"experience\":\"menengah\",\"personality\":\"introvert\"}"

# Test GET /history
curl http://localhost:5000/history
```

---

## 📁 File Structure

```
Smart Career Recommender/
├── frontend/
│   ├── index.html          # Form input page
│   ├── result.html         # Results display page
│   ├── style.css           # Global styling
│   └── test.html           # API testing page
├── backend/
│   ├── app.py              # Flask server & endpoints
│   ├── dataset.json        # Training data (25 samples)
│   ├── model.pkl           # Trained ML model
│   └── history.json        # Prediction history (auto-generated)
├── ml/
│   └── train_model.py      # ML training script
├── test_api.py             # API test script
├── requirements.txt        # Python dependencies
├── README.md               # Full documentation
└── QUICKSTART.md           # This file
```

---

## ⚙️ Configuration

### Change Port

Edit `backend/app.py` line terakhir:

```python
app.run(debug=True, port=5001)  # Change 5000 to any port you want
```

### Enable/Disable Debug Mode

Edit `backend/app.py`:

```python
app.run(debug=False)  # Set to False in production
```

---

## 🐛 Troubleshooting

### Error: "Port 5000 is already in use"

```bash
# Find process using port 5000
netstat -ano | findstr :5000

# Kill the process (replace PID with actual process ID)
taskkill /PID <PID> /F
```

Or use different port:
```python
app.run(debug=True, port=5001)
```

### Error: "No module named 'sklearn'" or other imports

Make sure virtual environment is activated and all packages installed:

```bash
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### Model not found error

Train the model first:

```bash
cd ml
python train_model.py
```

### CORS Error in browser

CORS is already enabled in `app.py` with `CORS(app)`. Make sure Flask-CORS is installed:

```bash
pip install Flask-CORS
```

### Frontend doesn't communicate with backend

1. Make sure backend server is running on `http://localhost:5000`
2. Check browser console for errors (F12)
3. Verify API_URL in index.html matches server address

---

## 📊 API Documentation

### Base URL
```
http://localhost:5000
```

### Endpoints

#### 1. GET /api/options
Get available form options

**Response:**
```json
{
  "success": true,
  "interests": ["administrasi", "desain", ...],
  "experiences": ["pemula", "menengah", "senior"],
  "personalities": ["introvert", "ambivert", "extrovert"],
  "skills": ["adobe", "analytics", ...]
}
```

#### 2. POST /predict
Get job recommendations

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
      "roadmap": "Python/JavaScript → Database → API → DevOps"
    }
  ]
}
```

#### 3. GET /history
Get prediction history

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

---

## 🎯 Features

✅ Machine Learning Model (Decision Tree)
✅ Rule-Based Recommendation Engine
✅ 25 Training Samples
✅ 25 Different Job Recommendations
✅ Skill Matching & Learning Roadmaps
✅ Prediction History Tracking
✅ Responsive UI (Mobile-friendly)
✅ Clean & Modern Design

---

## 📈 Test Results

```
TEST 1: Get Available Options
✓ Options loaded successfully
  - Interests: 5 options
  - Experiences: 3 options
  - Personalities: 3 options
  - Skills: 40 options

TEST 2: Prediction - Introvert Designer
✓ Prediction successful
  1. Video Editor - Score: 96%
  2. Graphic Designer - Score: 80%
  3. UI/UX Designer - Score: 30%

TEST 3: Prediction - Extrovert Marketer
✓ Prediction successful
  1. Digital Marketing Manager - Score: 80%
  2. PPC Specialist - Score: 30%

TEST 4: Prediction - Tech-savvy Introvert
✓ Prediction successful
  1. Backend Developer - Score: 80%
  2. Data Analyst - Score: 30%

TEST 5: Get History
✓ History retrieved successfully
  Total records: 3
```

---

## 💡 Next Steps

1. Try the application in browser
2. Test different combinations of inputs
3. Check prediction history
4. Customize skills and jobs in `backend/dataset.json`
5. Retrain model with new data
6. Deploy to production server

---

## 📝 Notes

- Model is trained on 25 samples covering various career paths
- Rule-based engine adds logical rules based on personality & interests
- Score calculation considers skill matching
- History is saved locally in JSON format
- Max 50 predictions stored in history

---

**Aplikasi sudah siap digunakan! 🎉**
