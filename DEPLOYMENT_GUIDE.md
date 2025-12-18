# Smart Career Recommender - Deployment Guide

## 🚀 Quick Deploy to Railway

### Step 1: Push to GitHub
```bash
# Create GitHub repository
# Copy this project to GitHub repo
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin master
```

### Step 2: Deploy to Railway
1. Go to [Railway.app](https://railway.app)
2. Sign up/Login with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Railway will auto-detect Python app and deploy

### Step 3: Configure Environment Variables (Optional)
In Railway dashboard:
- Go to Variables tab
- Add if needed:
  - `USE_LLM=false`
  - `FALLBACK_TO_DATABASE=true`
  - `GEMINI_API_KEY=your_key` (if using AI features)

### Step 4: Access Your App
Railway will provide a URL like: `https://your-app-name.up.railway.app`

## 🛠️ Alternative Deployment Options

### Option 2: Heroku
```bash
# Install Heroku CLI
heroku create your-app-name
git push heroku master
```

### Option 3: Render
1. Go to [Render.com](https://render.com)
2. New Web Service → Connect GitHub
3. Select Python, set build command: `pip install -r requirements.txt`
4. Start command: `python backend/app.py`

### Option 4: Local Hosting
```bash
cd backend
python app.py
# Access at http://localhost:5000
```

## 📋 Requirements
- Python 3.8+
- Dependencies in `requirements.txt`
- Model file `backend/model.pkl`
- Dataset `backend/dataset.json`

## 🔧 Troubleshooting

### App not starting
- Check Railway logs
- Ensure all files are committed
- Verify requirements.txt is correct

### Static files not loading
- Frontend files should be in `backend/static/`
- Routes are configured in `app.py`

### Model errors
- Ensure `model.pkl` is in `backend/` folder
- Retrain if needed: `python ml/train_model.py`

## 📞 Support
If deployment fails, check:
1. Railway build logs
2. Python version compatibility
3. Missing environment variables