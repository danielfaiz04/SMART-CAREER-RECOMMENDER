from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pickle
import json
import numpy as np
from datetime import datetime
import os
from dotenv import load_dotenv
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Serve static files
@app.route('/')
def index():
    return send_from_directory('backend/static', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('backend/static', path)

# Get the directory where app.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load environment variables
load_dotenv(os.path.join(BASE_DIR, 'backend', '.env'))

# Configure Gemini API
USE_LLM = os.getenv('USE_LLM', 'false').lower() == 'true'
FALLBACK_TO_DATABASE = os.getenv('FALLBACK_TO_DATABASE', 'true').lower() == 'true'
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')

if USE_LLM and GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        llm_model = genai.GenerativeModel('gemini-pro')
        print("✅ Gemini API configured successfully")
    except Exception as e:
        print(f"⚠️ Failed to configure Gemini API: {e}")
        USE_LLM = False
else:
    llm_model = None
    if not GEMINI_API_KEY:
        print("⚠️ GEMINI_API_KEY not found. LLM features disabled.")
    print("ℹ️ Using fallback database responses")

# Load trained model and encoders
model_path = os.path.join(BASE_DIR, 'backend', 'model.pkl')
with open(model_path, 'rb') as f:
    model_data = pickle.load(f)

model = model_data['model']
interest_encoder = model_data['interest_encoder']
experience_encoder = model_data['experience_encoder']
personality_encoder = model_data['personality_encoder']
job_encoder = model_data['job_encoder']
mlb = model_data['mlb']

# Load dataset for skill recommendations
dataset_path = os.path.join(BASE_DIR, 'backend', 'dataset.json')
with open(dataset_path, 'r') as f:
    training_data = json.load(f)

# Define skill roadmaps
skill_roadmaps = {
    "Graphic Designer": ["Kuasai Canva → Belajar Adobe Creative → Editing lanjutan → Portfolio design"],
    "Digital Marketing Manager": ["Copywriting dasar → Social media strategy → Analytics tools → Paid ads"],
    "Admin Officer": ["MS Office expert → File management → Office automation → Communication skills"],
    "Backend Developer": ["Python/JavaScript fundamentals → Database design → API development → DevOps"],
    "UI/UX Designer": ["Design principles → Figma mastery → User research → Prototyping"],
    "Sales Executive": ["Communication skills → Product knowledge → Negotiation → CRM tools"],
    "IT Support Specialist": ["Networking basics → Troubleshooting → Hardware knowledge → Ticketing systems"],
    "Office Manager": ["Project management → MS Office → Communication → Leadership"],
    "SEO Specialist": ["SEO fundamentals → Keyword research → Google Analytics → Technical SEO"],
    "Video Editor": ["Video editing software → Color grading → Audio editing → Motion graphics"],
    "Business Development Manager": ["Market research → Negotiation → Strategic planning → CRM"],
    "Frontend Developer": ["HTML/CSS → JavaScript → React → Responsive design"],
    "Data Entry Operator": ["Typing speed → MS Excel → Data accuracy → Attention to detail"],
    "Content Creator": ["Content planning → Writing → Social media → Video creation"],
    "Brand Designer": ["Brand strategy → Logo design → Visual identity → Branding guidelines"],
    "Data Analyst": ["SQL → Python → Data visualization → Statistical analysis"],
    "Customer Service Representative": ["Communication → Product knowledge → Problem solving → Empathy"],
    "Marketing Automation Specialist": ["Email marketing → Automation tools → Analytics → Lead nurturing"],
    "Web Designer": ["HTML/CSS → Responsive design → UX principles → Web accessibility"],
    "DevOps Engineer": ["Linux → Docker → Kubernetes → CI/CD → Cloud platforms"],
    "Project Coordinator": ["Project management tools → Communication → Timeline management → Risk management"],
    "Account Executive": ["Client relationship → Negotiation → Sales process → Account management"],
    "PPC Specialist": ["Google Ads → Facebook Ads → Conversion tracking → A/B testing"],
    "Motion Graphics Designer": ["After Effects → Animation principles → Motion design → 3D basics"],
    "Machine Learning Engineer": ["Python → Mathematics → Machine learning frameworks → Deep learning"]
}

# Define skills needed for each job
job_skills_required = {
    "Graphic Designer": ["canva", "editing", "design", "adobe"],
    "Digital Marketing Manager": ["copywriting", "social media", "marketing", "analytics"],
    "Admin Officer": ["ms office", "organization", "communication"],
    "Backend Developer": ["programming", "database", "api", "backend"],
    "UI/UX Designer": ["figma", "prototyping", "ux", "design"],
    "Sales Executive": ["komunikasi", "persuasi", "sales"],
    "IT Support Specialist": ["networking", "troubleshooting", "it", "technical"],
    "Office Manager": ["project management", "ms office", "organization"],
    "SEO Specialist": ["seo", "analytics", "marketing", "content"],
    "Video Editor": ["video editing", "adobe", "editing"],
    "Business Development Manager": ["komunikasi", "persuasi", "strategy"],
    "Frontend Developer": ["programming", "web development", "javascript"],
    "Data Entry Operator": ["data entry", "ms office", "accuracy"],
    "Content Creator": ["content writing", "social media", "communication"],
    "Brand Designer": ["branding", "illustration", "design"],
    "Data Analyst": ["data analysis", "sql", "python", "analytics"],
    "Customer Service Representative": ["customer service", "komunikasi", "empathy"],
    "Marketing Automation Specialist": ["email marketing", "automation", "analytics"],
    "Web Designer": ["web design", "ux research", "html", "css"],
    "DevOps Engineer": ["cloud computing", "devops", "linux", "docker"],
    "Project Coordinator": ["project management", "organization", "communication"],
    "Account Executive": ["komunikasi", "persuasi", "sales"],
    "PPC Specialist": ["paid ads", "google ads", "analytics"],
    "Motion Graphics Designer": ["motion graphics", "animation", "adobe"],
    "Machine Learning Engineer": ["machine learning", "python", "programming"]
}

# Rule-based recommendations
def get_rule_based_recommendations(interest, skills, experience, personality):
    """Apply rules to get job recommendations"""
    recommendations = []
    
    # Rule 1: Introvert + Design → Graphic Designer, UI/UX Designer
    if personality == "introvert" and interest == "desain":
        recommendations.extend(["Graphic Designer", "UI/UX Designer", "Video Editor"])
    
    # Rule 2: Extrovert + Marketing → Digital Marketing, Sales
    if personality == "extrovert" and interest == "marketing":
        recommendations.extend(["Digital Marketing Manager", "PPC Specialist"])
    
    # Rule 3: Extrovert + Sales → Sales Executive
    if personality == "extrovert" and interest == "penjualan":
        recommendations.extend(["Sales Executive", "Account Executive", "Business Development Manager"])
    
    # Rule 4: Admin skills + Office experience
    if "ms office" in skills and interest == "administrasi":
        recommendations.extend(["Admin Officer", "Office Manager", "Project Coordinator"])
    
    # Rule 5: Tech skills + Technology interest
    if interest == "teknologi":
        if any(skill in skills for skill in ["programming", "database"]):
            recommendations.extend(["Backend Developer", "Data Analyst"])
        if any(skill in skills for skill in ["networking", "troubleshooting"]):
            recommendations.extend(["IT Support Specialist", "DevOps Engineer"])
        if any(skill in skills for skill in ["machine learning", "python"]):
            recommendations.append("Machine Learning Engineer")
    
    # Rule 6: Data entry + Admin = Data Entry Operator
    if "data entry" in skills and experience == "pemula":
        recommendations.append("Data Entry Operator")
    
    # Rule 7: Frontend skills
    if any(skill in skills for skill in ["web development", "html"]):
        recommendations.extend(["Frontend Developer", "Web Designer"])
    
    # Rule 8: Content + Marketing = Content Creator
    if "content writing" in skills and interest == "marketing":
        recommendations.append("Content Creator")
    
    # Rule 9: Ambivert + Marketing = Marketing specialist roles
    if personality == "ambivert" and interest == "marketing":
        recommendations.extend(["SEO Specialist", "Marketing Automation Specialist", "Content Creator"])
    
    return list(set(recommendations))  # Remove duplicates

def calculate_match_score(job_title, user_skills):
    """Calculate skill match score for a job"""
    required_skills = job_skills_required.get(job_title, [])
    if not required_skills:
        return 50
    
    matched = sum(1 for skill in required_skills if any(user_skill.lower() in skill.lower() or skill.lower() in user_skill.lower() for user_skill in user_skills))
    score = (matched / len(required_skills)) * 100
    return min(100, int(score) + 30)  # Add base score

def get_skills_to_learn(job_title, user_skills):
    """Get skills user needs to learn for a specific job"""
    required_skills = job_skills_required.get(job_title, [])
    skills_to_learn = []
    
    for skill in required_skills:
        if not any(user_skill.lower() in skill.lower() or skill.lower() in user_skill.lower() for user_skill in user_skills):
            skills_to_learn.append(skill)
    
    return skills_to_learn[:3]  # Return top 3 skills

@app.route('/predict', methods=['POST'])
def predict():
    """Main prediction endpoint"""
    try:
        data = request.json
        interest = data.get('interest', '').lower()
        skills = [s.lower() for s in data.get('skills', [])]
        experience = data.get('experience', '').lower()
        personality = data.get('personality', '').lower()
        
        # Get rule-based recommendations
        rule_recommendations = get_rule_based_recommendations(interest, skills, experience, personality)
        
        # Get ML predictions
        try:
            interest_enc = interest_encoder.transform([interest])[0]
            experience_enc = experience_encoder.transform([experience])[0]
            personality_enc = personality_encoder.transform([personality])[0]
            skills_enc = mlb.transform([skills])[0]
            
            X_input = np.hstack([
                np.array([interest_enc]),
                np.array([experience_enc]),
                np.array([personality_enc]),
                skills_enc.reshape(1, -1)
            ])
            
            # Get predictions with probabilities
            predictions = model.predict(X_input)[0]
            predicted_job = job_encoder.inverse_transform([predictions])[0]
            
            # Combine rule-based and ML predictions
            all_jobs = list(set(rule_recommendations + [predicted_job]))
        except:
            # Fallback if encoding fails
            all_jobs = rule_recommendations if rule_recommendations else ["Graphic Designer", "IT Support Specialist", "Admin Officer"]
        
        # Generate detailed recommendations
        results = []
        for job in all_jobs[:3]:  # Top 3 recommendations
            match_score = calculate_match_score(job, skills)
            skills_to_learn = get_skills_to_learn(job, skills)
            roadmap = skill_roadmaps.get(job, "Lanjutkan pengembangan skill yang relevan dengan posisi")
            
            results.append({
                "title": job,
                "score": match_score,
                "skills_to_learn": skills_to_learn,
                "roadmap": roadmap
            })
        
        # Sort by score
        results = sorted(results, key=lambda x: x['score'], reverse=True)
        
        # Save to history
        save_to_history({
            "interest": interest,
            "skills": skills,
            "experience": experience,
            "personality": personality,
            "results": results
        })
        
        return jsonify({
            "success": True,
            "jobs": results
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400

@app.route('/history', methods=['GET'])
def get_history():
    """Get prediction history"""
    try:
        history_path = os.path.join(BASE_DIR, 'backend', 'history.json')
        if os.path.exists(history_path):
            with open(history_path, 'r') as f:
                history = json.load(f)
            return jsonify({
                "success": True,
                "history": history
            })
        return jsonify({
            "success": True,
            "history": []
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400

def save_to_history(prediction_data):
    """Save prediction to history file"""
    history = []
    history_path = os.path.join(BASE_DIR, 'backend', 'history.json')
    
    if os.path.exists(history_path):
        try:
            with open(history_path, 'r') as f:
                history = json.load(f)
        except:
            history = []
    
    # Add timestamp
    prediction_data['timestamp'] = datetime.now().isoformat()
    history.append(prediction_data)
    
    # Keep only last 50 records
    history = history[-50:]
    
    with open(history_path, 'w') as f:
        json.dump(history, f, indent=2)

@app.route('/api/options', methods=['GET'])
def get_options():
    """Get available options for form dropdowns"""
    interests = list(set([entry['interest'] for entry in training_data]))
    experiences = list(set([entry['experience'] for entry in training_data]))
    personalities = ["introvert", "ambivert", "extrovert"]
    
    all_skills = set()
    for entry in training_data:
        all_skills.update(entry['skills'])
    
    return jsonify({
        "success": True,
        "interests": sorted(interests),
        "experiences": sorted(experiences),
        "personalities": personalities,
        "skills": sorted(list(all_skills))
    })

# ============================================================================
# LLM Helper Functions
# ============================================================================

def call_gemini_api(prompt, max_retries=2):
    """Call Gemini API with retry logic"""
    if not USE_LLM or not llm_model:
        return None
    
    for attempt in range(max_retries):
        try:
            response = llm_model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Gemini API error (attempt {attempt + 1}/{max_retries}): {e}")
            if attempt == max_retries - 1:
                return None
    return None

def generate_job_explanation_with_llm(job_title, user_skills=None, user_experience=None):
    """Generate comprehensive job explanation using LLM"""
    skills_context = f" User has skills: {', '.join(user_skills)}" if user_skills else ""
    experience_context = f" Experience level: {user_experience}" if user_experience else ""
    
    prompt = f"""Anda adalah Career Advisor AI yang expert. Berikan penjelasan lengkap tentang pekerjaan "{job_title}" dalam format JSON.
{skills_context}{experience_context}

Berikan response dalam format JSON berikut (HARUS valid JSON, tanpa markdown):
{{
  "description": "Deskripsi lengkap pekerjaan ini (2-3 kalimat)",
  "why_suitable": ["Alasan 1 kenapa cocok", "Alasan 2", "Alasan 3"],
  "salary_range": "Rp X - Rp Y/bulan (untuk Indonesia)",
  "skills_required": [
    {{"skill": "Nama skill 1", "description": "Penjelasan skill"}},
    {{"skill": "Nama skill 2", "description": "Penjelasan skill"}},
    {{"skill": "Nama skill 3", "description": "Penjelasan skill"}},
    {{"skill": "Nama skill 4", "description": "Penjelasan skill"}},
    {{"skill": "Nama skill 5", "description": "Penjelasan skill"}}
  ],
  "pros": ["Keuntungan 1", "Keuntungan 2", "Keuntungan 3", "Keuntungan 4", "Keuntungan 5"],
  "cons": ["Tantangan 1", "Tantangan 2", "Tantangan 3", "Tantangan 4", "Tantangan 5"],
  "career_prospect": "Penjelasan prospek karir (2-3 kalimat)",
  "next_steps": ["Langkah 1", "Langkah 2", "Langkah 3", "Langkah 4", "Langkah 5", "Langkah 6"]
}}

Pastikan response adalah valid JSON tanpa backticks atau markdown."""
    
    response_text = call_gemini_api(prompt)
    
    if response_text:
        try:
            # Clean response (remove markdown if present)
            cleaned = response_text.strip()
            if cleaned.startswith('```'):
                # Remove markdown code blocks
                lines = cleaned.split('\n')
                cleaned = '\n'.join([l for l in lines if not l.strip().startswith('```')])
            
            # Parse JSON
            data = json.loads(cleaned)
            return data
        except json.JSONDecodeError as e:
            print(f"Failed to parse LLM JSON response: {e}")
            print(f"Response was: {response_text[:200]}...")
            return None
    
    return None

def generate_chat_response_with_llm(user_message, job_context=None, conversation_history=None):
    """Generate chat response using LLM"""
    context = f"\nKonteks: User sedang mempertimbangkan posisi '{job_context}'." if job_context else ""
    history = ""
    if conversation_history:
        history = "\n\nRiwayat percakapan:\n" + "\n".join(conversation_history[-5:])  # Last 5 messages
    
    prompt = f"""Anda adalah Career Advisor AI yang berpengalaman dan helpful. Jawab pertanyaan user dengan:
- Profesional namun friendly
- Spesifik dan actionable
- Gunakan emoji yang sesuai
- Format dengan bullet points atau numbering jika perlu
- Maksimal 300 kata{context}{history}

Pertanyaan user: {user_message}

Jawaban Anda:"""
    
    response = call_gemini_api(prompt)
    return response if response else None

# ============================================================================
# API Endpoints
# ============================================================================

# New Feature: Job Details with AI Explanation
@app.route('/job-details', methods=['POST'])
def job_details():
    """Provide detailed job information with AI explanation"""
    data = request.json
    job_title = data.get('job_title', 'Unknown')
    job_data = data.get('job_data', {})
    
    # Job details database
    job_details_db = {
        "Software Developer": {
            "description": "Seorang Software Developer bertanggung jawab untuk merancang, mengembangkan, dan memelihara aplikasi dan sistem perangkat lunak. Mereka bekerja dengan bahasa pemrograman, framework, dan tools terbaru untuk membangun solusi yang scalable dan efficient.",
            "why_suitable": [
                "Anda memiliki dasar pemrograman yang kuat",
                "Skill teknis Anda mencakup bahasa pemrograman utama",
                "Pengalaman Anda sesuai dengan kebutuhan role ini"
            ],
            "salary_range": "Rp 6.000.000 - Rp 20.000.000/bulan",
            "skills_required": [
                {"skill": "Python/Java/JavaScript", "description": "Bahasa pemrograman utama untuk development"},
                {"skill": "Database & SQL", "description": "Kemampuan mengelola database dan query optimization"},
                {"skill": "Version Control (Git)", "description": "Essential untuk collaborative development"},
                {"skill": "API Design & REST", "description": "Membuat dan mengintegrasikan API yang robust"},
                {"skill": "Testing & Debugging", "description": "Memastikan kualitas code dan error handling"}
            ],
            "pros": [
                "Demand pasar sangat tinggi dan job security terjamin",
                "Potensi earning yang sangat baik",
                "Terus belajar teknologi terbaru",
                "Fleksibilitas work dari mana saja (remote-friendly)",
                "Banyak kesempatan untuk advancement dan specialization"
            ],
            "cons": [
                "Deadline yang tight dan tekanan pekerjaan tinggi",
                "Ongoing learning requirement yang demanding",
                "Debugging bisa memakan waktu dan frustrasi",
                "Burnout risk jika tidak manage work-life balance",
                "Teknologi berubah cepat, harus selalu update"
            ],
            "career_prospect": "Karir sebagai developer memiliki prospek sangat cerah. Anda bisa menjadi Senior Developer, Tech Lead, Architect, atau beralih ke Product Management/Startup Founder.",
            "next_steps": [
                "Perkuat fundamentals: algoritma, data structure, design patterns",
                "Build project portfolio yang impressive di GitHub",
                "Kuasai 2-3 tech stack yang trending (React, Node.js, etc)",
                "Praktik problem solving di LeetCode/HackerRank",
                "Siapkan interview technical dengan mock interviews",
                "Network dengan developer lain melalui communities"
            ]
        },
        "Data Scientist": {
            "description": "Data Scientist menggunakan statistik, programming, dan machine learning untuk mengekstrak insights dari data dan membantu business decision making. Mereka bekerja dengan data exploration, modeling, dan visualization.",
            "why_suitable": [
                "Anda memiliki kemampuan analitik yang kuat",
                "Python dan statistical knowledge Anda cukup",
                "Passion untuk data analysis sangat terlihat"
            ],
            "salary_range": "Rp 7.000.000 - Rp 22.000.000/bulan",
            "skills_required": [
                {"skill": "Python/R & Data Libraries", "description": "Pandas, NumPy, Scikit-learn untuk data manipulation"},
                {"skill": "Statistics & Math", "description": "Probabilitas, inferensi statistik, linear algebra"},
                {"skill": "Machine Learning", "description": "Supervised learning, unsupervised learning, model evaluation"},
                {"skill": "Data Visualization", "description": "Matplotlib, Seaborn, Tableau untuk communicate insights"},
                {"skill": "SQL & Databases", "description": "Query data dari berbagai sumber dan data engineering basics"}
            ],
            "pros": [
                "Role yang sangat demanded di industri modern",
                "Kesempatan untuk solve real business problems",
                "Salary dan benefits yang competitive",
                "Terus learn tentang cutting-edge AI/ML",
                "High impact pada business decision making"
            ],
            "cons": [
                "Data quality issues sering menghambat project",
                "Model training bisa consuming resources & time",
                "Gap antara model dan production deployment",
                "Requires strong math background yang challenging",
                "Balancing antara theory dan practical implementation"
            ],
            "career_prospect": "Data Scientists sangat diperlukan di semua industri. Bisa evolve menjadi ML Engineer, Analytics Lead, atau Chief Data Officer.",
            "next_steps": [
                "Master Python, pandas, NumPy, scikit-learn thoroughly",
                "Pelajari statistics dan linear algebra dengan mendalam",
                "Kerjakan real datasets dari Kaggle competitions",
                "Buat end-to-end ML projects dan publish",
                "Belajar big data tools (Spark, Hadoop) untuk enterprise scale",
                "Deep learning dengan TensorFlow/PyTorch jika interested"
            ]
        },
        "Product Manager": {
            "description": "Product Manager bertanggung jawab untuk strategizing, developing, dan marketing produk. Mereka menjadi bridge antara customer, engineering, dan business. Mereka focus pada product vision dan execution.",
            "why_suitable": [
                "Leadership dan communication skills Anda sangat bagus",
                "Anda paham business strategy dan market trends",
                "Kemampuan decision making Anda solid"
            ],
            "salary_range": "Rp 8.000.000 - Rp 25.000.000/bulan",
            "skills_required": [
                {"skill": "Product Strategy", "description": "Membuat product vision, roadmap, dan prioritization"},
                {"skill": "User Research", "description": "Memahami user needs melalui research dan feedback"},
                {"skill": "Analytics & Metrics", "description": "Tracking KPI dan menggunakan data untuk decisions"},
                {"skill": "Communication", "description": "Present ideas, align stakeholders, provide clarity"},
                {"skill": "Leadership", "description": "Influence tanpa authority dan manage teams"}
            ],
            "pros": [
                "Sangat impactful - mempengaruhi jutaan users",
                "Diverse work melibatkan berbagai skill sets",
                "Compensation dan status dalam industri tech sangat baik",
                "Opportunities untuk entrepreneurship dan ownership",
                "Continuous learning tentang business dan technology"
            ],
            "cons": [
                "Ambiguous role dengan conflicting priorities",
                "Dealing dengan politics dan stakeholder management complex",
                "Failure rate tinggi - tidak semua products succeed",
                "High stress dengan multiple dependencies",
                "Technical skills tidak begitu di-appreciate despite importance"
            ],
            "career_prospect": "PM dengan track record bisa menjadi Director of Product, Chief Product Officer, atau start own company. Sangat valued di tech industry.",
            "next_steps": [
                "Pelajari product management frameworks dan methodologies",
                "Deepen understanding tentang your industry/market",
                "Build skills dalam data analysis dan metrics",
                "Practice user research dan customer interviews",
                "Develop business acumen dan understanding P&L",
                "Network dengan PMs dari leading tech companies"
            ]
        }
    }
    
    # Get job details atau gunakan default
    details = job_details_db.get(job_title, {
        "description": f"{job_title} adalah posisi yang menarik dengan prospek karir yang bagus. Posisi ini memerlukan dedikasi dan continuous learning untuk berkembang.",
        "why_suitable": [
            "Skill dan experience Anda match dengan requirements",
            "Career path Anda aligned dengan posisi ini"
        ],
        "salary_range": "Rp 5.000.000 - Rp 15.000.000/bulan",
        "skills_required": [
            {"skill": "Core Skills", "description": "Dasar-dasar yang diperlukan untuk posisi ini"},
            {"skill": "Advanced Skills", "description": "Skills lanjutan untuk standout di role ini"}
        ],
        "pros": [
            "Good career growth potential",
            "Interesting and challenging work"
        ],
        "cons": [
            "Requires continuous learning",
            "Market competition is increasing"
        ],
        "career_prospect": f"Career dalam {job_title} memiliki prospek yang bagus dengan banyak opportunities untuk growth dan specialization.",
        "next_steps": [
            "Improve relevant skills",
            "Build professional network",
            "Create strong portfolio",
            "Prepare for interview",
            "Stay updated with industry trends"
        ]
    })
    
    return jsonify(details)

@app.route('/api/explain_job', methods=['POST'])
def explain_job_with_ai():
    """Generate job explanation using LLM API"""
    try:
        data = request.json
        job_title = data.get('job', '')
        user_skills = data.get('skills', [])
        user_experience = data.get('experience', '')
        
        if not job_title:
            return jsonify({
                "success": False,
                "error": "Job title is required"
            }), 400
        
        # Try LLM first
        llm_response = None
        if USE_LLM:
            llm_response = generate_job_explanation_with_llm(job_title, user_skills, user_experience)
        
        # Use LLM response if available, otherwise fallback to database
        if llm_response:
            return jsonify({
                "success": True,
                "source": "ai",
                **llm_response
            })
        elif FALLBACK_TO_DATABASE:
            # Fallback to static database
            job_details_db = {
                "Graphic Designer": {
                    "description": "Graphic Designer menciptakan visual content untuk berbagai media. Mereka menggunakan software design untuk membuat logo, marketing materials, dan brand identity.",
                    "why_suitable": [
                        "Anda memiliki kreativitas dan eye for design",
                        "Skill visual Anda cocok untuk role ini",
                        "Portfolio Anda menunjukkan potensi yang bagus"
                    ],
                    "salary_range": "Rp 4.000.000 - Rp 12.000.000/bulan",
                    "skills_required": [
                        {"skill": "Adobe Creative Suite", "description": "Photoshop, Illustrator, InDesign untuk design work"},
                        {"skill": "Typography", "description": "Pemahaman font pairing dan hierarchy"},
                        {"skill": "Color Theory", "description": "Penggunaan warna yang efektif"},
                        {"skill": "Layout Design", "description": "Komposisi visual yang menarik"},
                        {"skill": "Branding", "description": "Memahami brand identity dan consistency"}
                    ],
                    "pros": [
                        "Kreativitas tanpa batas",
                        "Portfolio yang impressive",
                        "Freelance opportunities banyak",
                        "Remote work friendly",
                        "Industri yang terus berkembang"
                    ],
                    "cons": [
                        "Deadline yang ketat",
                        "Revisi yang banyak dari client",
                        "Kompetisi yang tinggi",
                        "Perlu update skill terus",
                        "Gaji awal relatif rendah"
                    ],
                    "career_prospect": "Graphic Designer bisa berkembang menjadi Art Director, Creative Director, atau memulai design agency sendiri. Demand untuk designer terus meningkat.",
                    "next_steps": [
                        "Master Adobe Creative Suite",
                        "Build portfolio yang strong",
                        "Belajar design principles",
                        "Join design communities",
                        "Practice dengan real projects",
                        "Stay updated dengan design trends"
                    ]
                },
                "Backend Developer": {
                    "description": "Backend Developer membangun server-side logic, database, dan API yang menjadi fondasi aplikasi. Fokus pada performance, security, dan scalability.",
                    "why_suitable": [
                        "Skill programming Anda solid",
                        "Logical thinking Anda kuat",
                        "Anda suka problem solving"
                    ],
                    "salary_range": "Rp 6.000.000 - Rp 20.000.000/bulan",
                    "skills_required": [
                        {"skill": "Programming Languages", "description": "Python, Java, Node.js, atau Go"},
                        {"skill": "Database Management", "description": "SQL, NoSQL, query optimization"},
                        {"skill": "API Development", "description": "RESTful API, GraphQL design"},
                        {"skill": "Version Control", "description": "Git workflow dan collaboration"},
                        {"skill": "Cloud Services", "description": "AWS, Google Cloud, atau Azure"}
                    ],
                    "pros": [
                        "High demand di job market",
                        "Salary yang competitive",
                        "Remote work opportunities",
                        "Continuous learning",
                        "Career growth yang jelas"
                    ],
                    "cons": [
                        "Deadline pressure tinggi",
                        "On-call duties kadang diperlukan",
                        "Debugging bisa frustrating",
                        "Technology berubah cepat",
                        "Burnout risk jika tidak manage well"
                    ],
                    "career_prospect": "Backend Developer bisa menjadi Senior Developer, Tech Lead, Software Architect, atau CTO. Banyak opportunities untuk specialization.",
                    "next_steps": [
                        "Master satu bahasa pemrograman",
                        "Pelajari database design",
                        "Build API projects",
                        "Learn cloud platforms",
                        "Practice dengan open source",
                        "Prepare untuk technical interviews"
                    ]
                },
                "Video Editor": {
                    "description": "Video Editor bertanggung jawab merakit rekaman mentah menjadi produk video akhir yang menarik. Mereka memanipulasi video, audio, dan grafis untuk menceritakan kisah yang kohesif.",
                    "why_suitable": [
                        "Detail-oriented dan kreatif",
                        "Memiliki sense of timing dan rhythm yang baik",
                        "Tertarik dengan storytelling visual"
                    ],
                    "salary_range": "Rp 5.000.000 - Rp 15.000.000/bulan",
                    "skills_required": [
                        {"skill": "Adobe Premiere Pro/After Effects", "description": "Industry standard software"},
                        {"skill": "Color Grading", "description": "Mengatur mood visual"},
                        {"skill": "Audio Mixing", "description": "Menyeimbangkan suara dan musik"},
                        {"skill": "Storytelling", "description": "Menyusun narasi yang kuat"},
                        {"skill": "Motion Graphics", "description": "Menambahkan elemen grafis bergerak"}
                    ],
                    "pros": [
                        "Karya bisa dilihat banyak orang",
                        "Bisa bekerja freelance/remote",
                        "Industri kreatif yang fun",
                        "Potensi viral",
                        "Selalu ada teknologi baru"
                    ],
                    "cons": [
                        "Rendering time yang membosankan",
                        "Feedback klien yang subjektif",
                        "Deadline ketat",
                        "Hardware requirement tinggi",
                        "Kerja bisa sampai larut malam"
                    ],
                    "career_prospect": "Video Editor bisa menjadi Lead Editor, Motion Graphic Artist, atau Sutradara. Content consumption video terus naik tajam (TikTok, YouTube).",
                    "next_steps": [
                        "Buat showreel/portfolio terbaik",
                        "Pelajari teknik editing modern",
                        "Ikuti tren TikTok/Reels",
                        "Network dengan content creators",
                        "Kuasai dasar 3D animation"
                    ]
                },
                "Digital Marketing Manager": {
                    "description": "Digital Marketing Manager merencanakan dan mengeksekusi kampanye pemasaran digital. Mereka mengelola SEO, SEM, media sosial, dan email marketing untuk meningkatkan brand awareness dan sales.",
                    "why_suitable": [
                        "Analitis dan kreatif sekaligus",
                        "Suka dengan tren sosial media",
                        "Berorientasi pada data dan hasil"
                    ],
                    "salary_range": "Rp 7.000.000 - Rp 20.000.000/bulan",
                    "skills_required": [
                        {"skill": "SEO/SEM", "description": "Optimasi mesin pencari dan iklan berbayar"},
                        {"skill": "Social Media Strategy", "description": "Content planning dan engagement"},
                        {"skill": "Data Analytics", "description": "Membaca Google Analytics/Ads report"},
                        {"skill": "Copywriting", "description": "Menulis iklan yang menjual"},
                        {"skill": "Content Marketing", "description": "Strategi distribusi konten"}
                    ],
                    "pros": [
                        "Sangat dibutuhkan di semua industri",
                        "Dinamis dan tidak membosankan",
                        "Bisa diukur hasilnya (measurable)",
                        "Potensi gaji tinggi",
                        "Banyak tools yang membantu"
                    ],
                    "cons": [
                        "Algoritma platform sering berubah",
                        "Tekanan target KPI/ROI",
                        "Harus selalu online/update",
                        "Kompetisi market ketat",
                        "Budget management stress"
                    ],
                    "career_prospect": "Bisa menjadi CMO (Chief Marketing Officer), Head of Growth, atau Konsultan Digital Marketing.",
                    "next_steps": [
                        "Ambil sertifikasi Google/Meta Ads",
                        "Pelajari SEO mendalam",
                        "Mulai projek marketing kecil",
                        "Pahami funnel marketing",
                        "Analisis kampanye kompetitor"
                    ]
                }
            }
            
            details = job_details_db.get(job_title, {
                "description": f"{job_title} adalah posisi yang menarik dengan prospek karir yang bagus.",
                "why_suitable": [
                    "Skill Anda match dengan requirements",
                    "Experience Anda sesuai dengan posisi ini"
                ],
                "salary_range": "Rp 5.000.000 - Rp 15.000.000/bulan",
                "skills_required": [
                    {"skill": "Core Skills", "description": "Fundamental skills untuk posisi ini"},
                    {"skill": "Technical Skills", "description": "Skills teknis yang diperlukan"},
                    {"skill": "Soft Skills", "description": "Communication dan teamwork"}
                ],
                "pros": [
                    "Career growth potential",
                    "Interesting work",
                    "Good compensation"
                ],
                "cons": [
                    "Requires continuous learning",
                    "Market competition"
                ],
                "career_prospect": f"Career dalam {job_title} memiliki prospek yang bagus dengan opportunities untuk growth.",
                "next_steps": [
                    "Improve relevant skills",
                    "Build portfolio",
                    "Network dengan professionals",
                    "Prepare untuk interview"
                ]
            })
            
            return jsonify({
                "success": True,
                "source": "database",
                **details
            })
        else:
            return jsonify({
                "success": False,
                "error": "LLM unavailable and fallback disabled"
            }), 503
            
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# New Feature: Career Chat with AI
@app.route('/chat', methods=['POST'])
def chat():
    """Chat endpoint untuk career counseling dengan respons intelligent"""
    try:
        data = request.json
        message = data.get('message', '').strip()
        message_lower = message.lower()
        context = data.get('context')
        
        job_title = context.get('jobTitle') if context else None
        
        # Try LLM first
        if USE_LLM:
            llm_response = generate_chat_response_with_llm(message, job_title)
            if llm_response:
                return jsonify({
                    "success": True,
                    "response": llm_response,
                    "source": "ai"
                })
        
        # Fallback to keyword matching (Smart Fallback)
        response = ""
        
        # 1. Gaji / Salary
        if any(w in message_lower for w in ['gaji', 'salary', 'bayaran', 'penghasilan', 'uang']):
            if job_title:
                response = f"Untuk posisi **{job_title}**, estimasi gaji di Indonesia berkisar antara **Rp 5.000.000 - Rp 15.000.000** tergantung pengalaman dan lokasi. 💰\n\nTips negosiasi:\n- Riset standar gaji industri\n- Tunjukkan portfolio/pencapaian\n- Jangan ragu untuk negosiasi di angka yang wajar."
            else:
                response = "Secara umum, gaji sangat bergantung pada posisi, industri, dan pengalaman. Silakan sebutkan posisi spesifik yang ingin Anda ketahui range gajinya. 💰"
        
        # 2. Skill / Kemampuan
        elif any(w in message_lower for w in ['skill', 'kemampuan', 'bisa apa', 'belajar apa', 'syarat']):
            if job_title:
                response = f"Untuk sukses sebagai **{job_title}**, fokuslah mengembangkan skill ini:\n\n1. **Technical Skills**: Kuasai tools/software utama bidang ini\n2. **Soft Skills**: Komunikasi & problem solving\n3. **Industry Knowledge**: Pahami tren terbaru\n\nPerlu roadmap belajar yang lebih detail? 📚"
            else:
                response = "Setiap pekerjaan membutuhkan skill set berbeda. Hard skill (teknis) dan Soft skill (kepribadian) sama pentingnya! Posisi apa yang sedang Anda incar? 🎯"

        # 3. Interview / Wawancara
        elif any(w in message_lower for w in ['interview', 'wawancara', 'tes', 'pertanyaan']):
            response = "Tips Interview Jitu: 🎤\n\n1. **Riset Perusahaan**: Pahami visi misi mereka.\n2. **Metode STAR**: Jawab pertanyaan dengan (Situation, Task, Action, Result).\n3. **Siapkan Pertanyaan**: Tanya balik pewawancara untuk menunjukkan antusiasme.\n4. **Body Language**: Tampil percaya diri namun sopan.\n\nAnda mau simulasi pertanyaan interview untuk posisi tertentu?"

        # 4. Strategi Cari Kerja / CV
        elif any(w in message_lower for w in ['cari kerja', 'lamar', 'cv', 'portofolio', 'strategi']):
            response = "Strategi Job Search Efektif: 🔍\n\n1. **Optimasi LinkedIn**: Pastikan profil lengkap dan profesional.\n2. **Tailored CV**: Sesuaikan CV untuk setiap lamaran (gunakan kata kunci relevan!).\n3. **Networking**: Jangan malu menghubungi recruiter/koneksi secara sopan.\n4. **Build Portfolio**: Tunjukkan hasil karya nyata Anda.\n\nSemangat! Konsistensi adalah kunci. 💪"

        # 5. Default / Greeting / Other
        else:
            greetings = ["halo", "hi", "pagi", "siang", "sore", "malam"]
            if any(w in message_lower for w in greetings):
                response = f"Halo! 👋 Ada yang bisa saya bantu terkait karir Anda hari ini?"
            else:
                response = f"Pertanyaan menarik! 🤔\n\nJika ingin diskusi lebih dalam menggunakan AI, pastikan fitur LLM aktif. Saat ini saya bisa menjawab topik umum seputar:\n- 💰 Range Gaji\n- 🎯 Skill Development\n- 🎤 Tips Interview\n- 🔍 Strategi Job Search\n\nSilakan pilih topik di menu (☰) atau ketik pertanyaan spesifik!"

        return jsonify({
            "success": True,
            "response": response,
            "source": "keyword_matching"
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# ============================================================================
# Export Feature
# ============================================================================

@app.route('/api/export', methods=['POST'])
def export_recommendations():
    """Export recommendations to CSV format"""
    try:
        from io import StringIO
        import csv
        
        data = request.json
        jobs = data.get('jobs', [])
        user_info = data.get('user_info', {})
        
        # Create CSV in memory
        output = StringIO()
        output.write('\ufeff')  # BOM for Excel UTF-8 support
        
        writer = csv.writer(output)
        
        # Header
        writer.writerow(['Smart Career Recommender - Hasil Rekomendasi'])
        writer.writerow([''])
        writer.writerow(['Informasi User:'])
        writer.writerow(['Minat', user_info.get('interest', '-')])
        writer.writerow(['Skills', ', '.join(user_info.get('skills', []))])
        writer.writerow(['Pengalaman', user_info.get('experience', '-')])
        writer.writerow(['Kepribadian', user_info.get('personality', '-')])
        writer.writerow([''])
        writer.writerow(['Rekomendasi Karir:'])
        writer.writerow([''])
        
        # Job recommendations
        writer.writerow(['No', 'Posisi', 'Match Score', 'Skills to Learn', 'Roadmap'])
        
        for idx, job in enumerate(jobs, 1):
            writer.writerow([
                idx,
                job.get('title', ''),
                f"{job.get('score', 0)}%",
                ', '.join(job.get('skills_to_learn', [])) or '-',
                job.get('roadmap', '')
            ])
        
        csv_content = output.getvalue()
        output.close()
        
        return jsonify({
            'success': True,
            'data': csv_content,
            'filename': 'career_recommendations.csv'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Smart Career Recommender API running on port {port}")
    app.run(debug=False, host='0.0.0.0', port=port, threaded=True, use_reloader=False)

