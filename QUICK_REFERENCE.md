# Smart Career Recommender - QUICK REFERENCE GUIDE

## 🚀 Quick Start (2 Minutes)

### Setup
```bash
# Navigate to project
cd "c:\laragon\www\Smart Career Recommender"

# Install dependencies
pip install -r requirements.txt

# Start backend (leave running)
cd backend
python -m flask run --host 0.0.0.0 --port 5000 --no-reload
```

### Access Application
Open in browser:
```
file:///c:/laragon/www/Smart%20Career%20Recommender/frontend/index.html
```

**✅ Application Ready!**

---

## 📋 File Locations Quick Reference

| What | Where |
|------|-------|
| Main form | `frontend/index.html` |
| Results page | `frontend/result.html` |
| Styling | `frontend/style.css` |
| Flask API | `backend/app.py` |
| ML model | `backend/model.pkl` |
| Training data | `backend/dataset.json` |
| ML script | `ml/train_model.py` |
| Dependencies | `requirements.txt` |

---

## 🔌 API Quick Reference

### /api/options (GET)
Get available skills
```bash
curl http://127.0.0.1:5000/api/options
```
Returns: 40 skills

### /predict (POST)
Get recommendations
```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "interest": "Technology",
    "skills": ["Python", "JavaScript"],
    "experience": "3-5 years",
    "personality": "Analytical"
  }'
```
Returns: Top 3 job recommendations with scores

### /history (GET)
Get prediction history
```bash
curl http://127.0.0.1:5000/history
```
Returns: All past predictions

---

## 🧪 Testing Quick Reference

### Test All Endpoints
```bash
cd backend
python simple_test.py
```

### Retrain ML Model
```bash
cd ml
python train_model.py
```

### Verify Setup
```bash
python verify_setup.py
```

---

## ⚙️ Configuration Quick Reference

### Change Port
Edit `backend/app.py` line 298:
```python
app.run(host='0.0.0.0', port=5001)  # Change 5000 to 5001
```

### Change Debug Mode
In `backend/app.py`, change line 298:
```python
app.run(host='0.0.0.0', debug=True)  # For development
app.run(host='0.0.0.0', debug=False) # For production
```

### Add New Skills
1. Edit `backend/app.py` - Find `ALL_SKILLS` list (around line 30)
2. Add new skill to list
3. Update `backend/dataset.json` training data
4. Retrain model: `python ml/train_model.py`

### Add New Jobs
1. Edit `backend/dataset.json` - Add new job to samples
2. Retrain model: `python ml/train_model.py`
3. Update `result.html` if needed

---

## 📊 Project Status

| Component | Status |
|-----------|--------|
| Frontend | ✅ Complete |
| Backend | ✅ Complete |
| ML Model | ✅ Complete |
| API Endpoints | ✅ Complete (3/3) |
| Testing | ✅ Complete |
| Documentation | ✅ Complete |
| **Overall** | **✅ READY** |

---

## 🐛 Common Issues

| Problem | Solution |
|---------|----------|
| Port in use | Change port or kill process: `netstat -ano \| findstr 5000` |
| Module not found | Reinstall: `pip install -r requirements.txt` |
| No recommendations | Check backend logs or retrain model |
| Frontend blank | Check browser console for JS errors |
| Slow performance | Restart Flask server |

---

## 📱 Browser Compatibility

- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

---

## 🔒 Security Notes

✅ CORS enabled for frontend  
✅ No hardcoded credentials  
✅ Input validation on backend  
✅ Production mode enabled  

---

## 📝 Key Commands Cheat Sheet

```bash
# Install dependencies
pip install -r requirements.txt

# Start Flask server
cd backend && python -m flask run --host 0.0.0.0 --port 5000 --no-reload

# Test backend
cd backend && python simple_test.py

# Retrain ML model
cd ml && python train_model.py

# Check Python version
python --version

# Check installed packages
pip list | findstr Flask

# Activate virtual environment (if using venv)
..\venv\Scripts\activate

# Deactivate virtual environment
deactivate
```

---

## 🎯 Next Steps

1. **First Time:**
   - Run setup commands above
   - Open frontend in browser
   - Fill form and test

2. **Customization:**
   - Edit skills in app.py
   - Update dataset.json
   - Retrain model
   - Deploy

3. **Deployment:**
   - See DEPLOYMENT_CHECKLIST.md
   - See FINAL_STATUS.md for full docs

---

## 📞 Support Resources

| Resource | Location |
|----------|----------|
| Setup guide | QUICKSTART.md |
| Full status | FINAL_STATUS.md |
| Deployment | DEPLOYMENT_CHECKLIST.md |
| Architecture | ARCHITECTURE.md |
| Project details | PROJECT_SUMMARY.md |
| README | README.md |

---

## ✅ Verification Checklist

Before deploying:
- [ ] `pip install -r requirements.txt` runs without errors
- [ ] `python -m flask run` starts server on port 5000
- [ ] `simple_test.py` shows all 3 endpoints pass
- [ ] Frontend loads in browser
- [ ] Form submission works
- [ ] Results page displays recommendations

---

**Quick Start Guide v1.0**  
*Last Updated: November 29, 2025*  
**Status: ✅ READY TO USE**

