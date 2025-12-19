# 📚 Smart Career Recommender - User Manual

## 🌐 Live Application
**URL**: https://smart-career-production.up.railway.app/

## 🎯 Quick Start Guide

### Step 1: Access the Application
1. Open your web browser
2. Go to: https://smart-career-production.up.railway.app/
3. Wait for the page to load (may take 10-20 seconds on first visit)

### Step 2: Fill the Career Assessment Form

#### 🎯 Interest Selection
Choose one interest that matches your passion:
- **Desain** - Creative design work
- **Marketing** - Business and promotion
- **Administrasi** - Office and organizational work
- **Teknologi** - IT and programming
- **Penjualan** - Sales and customer interaction

#### 💻 Skills Selection
Check all skills you currently possess from the list of 40+ skills:
- Programming languages (Python, JavaScript, etc.)
- Design tools (Photoshop, Figma, etc.)
- Business skills (Marketing, Sales, etc.)
- Technical skills (Database, Networking, etc.)

#### 📊 Experience Level
Select your work experience:
- **Pemula** - Less than 1 year
- **Menengah** - 1-5 years
- **Senior** - More than 5 years

#### 🧠 Personality Type
Choose your personality type:
- **Introvert** - Prefer working alone, thoughtful
- **Ambivert** - Balance of social and independent
- **Extrovert** - Outgoing, enjoy social interaction

### Step 3: Get Recommendations
1. Click **"Dapatkan Rekomendasi"** button
2. Wait for AI processing (5-10 seconds)
3. View your personalized career recommendations

### Step 4: Review Results
Each recommendation includes:
- **Job Title** - Recommended career path
- **Match Score** - Percentage compatibility (0-100%)
- **Skills to Learn** - What you need to develop
- **Learning Roadmap** - Step-by-step improvement plan

## 📋 Features Overview

### 🤖 AI-Powered Recommendations
- Machine Learning model trained on career data
- Rule-based engine for logical recommendations
- Combines your input with industry standards

### 💾 History Tracking
- Click **"📋 Lihat Riwayat"** to see past recommendations
- View up to 50 previous assessments
- Track your career exploration journey

### 🎨 Modern Interface
- Responsive design (works on mobile/desktop)
- Dark/Light theme toggle
- Indonesian language interface
- Emoji-enhanced user experience

## 🔧 Troubleshooting

### Application Won't Load
- **Solution**: Hard refresh (Ctrl+F5 or Cmd+Shift+R)
- **Wait time**: Railway free tier may take 10-20 seconds to wake up
- **Check**: Ensure stable internet connection

### Form Won't Submit
- **Check**: All required fields are filled
- **Verify**: At least 1 skill is selected
- **Error**: Look for red error messages below form

### No Recommendations Received
- **Cause**: Usually due to incomplete form data
- **Fix**: Ensure all fields are properly selected
- **Retry**: Try different skill combinations

### Skills List Not Loading
- **Issue**: API connection problem
- **Solution**: Refresh the page
- **Check**: Browser console (F12) for network errors

## 📊 Understanding Your Results

### Match Score Interpretation
- **80-100%**: Excellent match - pursue this career
- **60-79%**: Good match - consider with some training
- **40-59%**: Moderate match - may need significant changes
- **0-39%**: Poor match - explore other options

### Skills to Learn
- **Top 3 skills** prioritized for your career path
- **Actionable items** you can start immediately
- **Time estimates** included where available

### Learning Roadmap
- **Phase 1**: Foundation skills (1-3 months)
- **Phase 2**: Intermediate skills (3-6 months)
- **Phase 3**: Advanced skills (6+ months)
- **Resources**: Suggested learning platforms

## 🌟 Advanced Features

### Career Chat (Coming Soon)
- AI-powered career counseling
- Ask questions about specific careers
- Get detailed explanations and advice

### Job Details (Coming Soon)
- Comprehensive job descriptions
- Salary ranges for Indonesian market
- Required qualifications and responsibilities

### Export Feature
- Download recommendations as CSV
- Share results with mentors/counselors
- Keep records for future reference

## 📞 Support & Contact

### For Technical Issues
- Check Railway status: https://status.railway.app/
- Review browser console for error messages
- Try different browsers (Chrome, Firefox, Safari)

### For Career Advice
- Use the recommendations as starting points
- Consult with career counselors for personalized advice
- Consider taking career assessment tests

### Feature Requests
- Current app focuses on Indonesian job market
- Future updates may include international careers
- AI features are continuously improving

## 🔄 Updates & Maintenance

### Version History
- **v1.0** - Initial deployment with core features
- **Future** - Enhanced AI, more job categories, chat features

### Data Updates
- Career data updated periodically
- New job categories added based on market trends
- Skills database expanded regularly

### Performance
- Free tier may have cold start delays
- Consider upgrading to paid plan for better performance
- Response times: 2-5 seconds for recommendations

## 📋 API Reference (For Developers)

### Endpoints Available
- `GET /api/options` - Get form options
- `POST /predict` - Get career recommendations
- `GET /history` - Get recommendation history
- `POST /job-details` - Get detailed job info (future)
- `POST /chat` - Career chat (future)

### Sample API Usage
```javascript
// Get recommendations
const response = await fetch('/predict', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    interest: 'teknologi',
    skills: ['programming', 'database'],
    experience: 'menengah',
    personality: 'introvert'
  })
});
```

## 🎉 Success Stories

Users have successfully used this app to:
- Discover new career paths they never considered
- Identify skills gaps and create learning plans
- Make informed decisions about career changes
- Find motivation and direction in their professional journey

## 📝 Terms of Use

- This app provides general career guidance
- Results are not guaranteed predictions
- Always consult professionals for important career decisions
- Data is processed securely and not stored permanently

---

**Last Updated**: December 19, 2025
**Version**: 1.0
**Status**: Live on Railway</content>
<parameter name="filePath">c:\laragon\www\Smart Career Recommender\USER_MANUAL.md