# 🚀 Smart Career Recommender - Setup Fitur Baru

## ⚡ Quick Start (5 Menit)

### 1. Install Dependencies
```bash
# Aktifkan virtual environment
.venv\Scripts\Activate.ps1

# Install library baru
pip install google-generativeai python-dotenv
```

### 2. Setup API Key

**Dapatkan Gemini API Key (GRATIS):**
1. Buka: https://makersuite.google.com/app/apikey
2. Login dengan Google Account
3. Klik "Create API Key"
4. Copy API key yang muncul

**Edit file `backend\.env`:**
```env
GEMINI_API_KEY=paste_api_key_disini
USE_LLM=true
```

### 3. Restart Server
```bash
# Stop server (Ctrl+C jika masih running)
python backend/app.py
```

**Cek output:**
```
✅ Gemini API configured successfully
Smart Career Recommender API running on http://localhost:5000
```

### 4. Test Aplikasi
1. Buka browser: `http://localhost:5000` atau buka `frontend/index.html`
2. Isi form rekomendasi
3. Klik "Detail Pekerjaan" → Lihat badge "✨ Powered by AI"
4. Klik "Tanya Career Advisor" → Chat dengan AI
5. Klik tombol 🌙/☀️ di pojok kanan atas → Toggle dark mode

---

## ✨ Fitur Baru

### 1. 🤖 AI Job Explanations
- Penjelasan pekerjaan yang dinamis dan detail
- Skills breakdown dengan penjelasan
- Estimasi gaji untuk Indonesia
- Pros & cons karir
- Career roadmap

### 2. 💬 AI Career Chat
- Chat dengan Career Advisor AI
- Respons kontekstual dan natural
- Quick suggestions
- Fallback ke keyword matching

### 3. 🌙 Dark/Light Mode
- Toggle theme di semua halaman
- Smooth transitions
- Auto-save preference
- System theme detection

### 4. 💼 LinkedIn Integration
- Tombol cari lowongan di LinkedIn
- Auto-search dengan job title

---

## 🔧 Troubleshooting

### API Key Tidak Berfungsi
```bash
# Cek file .env
cat backend\.env

# Pastikan formatnya benar (tanpa spasi atau quotes)
GEMINI_API_KEY=AIzaSy...
USE_LLM=true
```

### LLM Tidak Aktif
**Cek console backend**, harus ada:
```
✅ Gemini API configured successfully
```

Jika ada error:
```
⚠️ GEMINI_API_KEY not found. LLM features disabled.
ℹ️ Using fallback database responses
```
→ Berarti API key belum di-set dengan benar

### Aplikasi Tetap Berfungsi Tanpa API Key
✅ **Ya!** Semua fitur memiliki fallback:
- Job details → Database statis
- Chat → Keyword matching
- Aplikasi tidak akan crash

---

## 📁 File-File Penting

```
Smart Career Recommender/
├── backend/
│   ├── app.py              ← Modified (LLM integration)
│   ├── .env                ← NEW (API configuration)
│   └── .env.example        ← NEW (Template)
├── frontend/
│   ├── theme.css           ← NEW (Dark mode styles)
│   ├── theme.js            ← NEW (Theme manager)
│   ├── index.html          ← Modified (theme added)
│   ├── result.html         ← Modified (theme added)
│   ├── job-detail.html     ← Modified (new endpoint)
│   └── career-chat.html    ← Modified (LLM upgrade)
└── requirements.txt        ← Modified (new deps)
```

---

## 🎯 Mode Operasi

### Mode 1: Full AI (Recommended)
```env
USE_LLM=true
GEMINI_API_KEY=your_key_here
```
✅ AI job explanations
✅ AI chat responses
✅ Best user experience

### Mode 2: Fallback Only
```env
USE_LLM=false
```
✅ Database job details
✅ Keyword matching chat
✅ Tetap berfungsi sempurna

---

## 📚 Dokumentasi Lengkap

Lihat file artifact untuk detail:
- `implementation_plan.md` - Technical details
- `walkthrough.md` - Feature walkthrough
- `task.md` - Implementation checklist

---

## ✅ Checklist Verifikasi

- [ ] Dependencies ter-install (`pip list | grep generativeai`)
- [ ] File `.env` ada dan berisi API key
- [ ] Server restart dan ada pesan "✅ Gemini API configured"
- [ ] Badge "✨ Powered by AI" muncul di job details
- [ ] Chat memberikan respons yang natural
- [ ] Dark mode toggle berfungsi
- [ ] LinkedIn button membuka tab baru

---

## 💡 Tips

1. **API Key Gratis Gemini** memiliki rate limit, tapi cukup untuk development
2. **Fallback mechanism** memastikan app selalu berfungsi
3. **Dark mode preference** tersimpan di browser localStorage
4. **Chat context** hanya dalam session, tidak persistent

---

**🎉 Selamat! Aplikasi Career Recommender Anda sekarang lebih powerful dengan AI!**
