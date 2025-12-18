import requests
import json

API_URL = "http://localhost:5000"

# Test 1: Get API options
print("=" * 50)
print("TEST 1: Get Available Options")
print("=" * 50)
try:
    response = requests.get(f"{API_URL}/api/options")
    data = response.json()
    if data['success']:
        print("✓ Options loaded successfully")
        print(f"  - Interests: {len(data['interests'])} options")
        print(f"  - Experiences: {len(data['experiences'])} options")
        print(f"  - Personalities: {len(data['personalities'])} options")
        print(f"  - Skills: {len(data['skills'])} options")
    else:
        print("✗ Error:", data.get('error'))
except Exception as e:
    print(f"✗ Error: {e}")

# Test 2: Predict with user input 1
print("\n" + "=" * 50)
print("TEST 2: Prediction - Introvert Designer")
print("=" * 50)
try:
    payload = {
        "interest": "desain",
        "skills": ["canva", "editing"],
        "experience": "pemula",
        "personality": "introvert"
    }
    response = requests.post(f"{API_URL}/predict", json=payload)
    data = response.json()
    if data['success']:
        print("✓ Prediction successful")
        for i, job in enumerate(data['jobs'], 1):
            print(f"\n  {i}. {job['title']}")
            print(f"     Score: {job['score']}%")
            print(f"     Skills to learn: {', '.join(job['skills_to_learn'][:2])}")
            print(f"     Roadmap: {job['roadmap'][:50]}...")
    else:
        print("✗ Error:", data.get('error'))
except Exception as e:
    print(f"✗ Error: {e}")

# Test 3: Predict with user input 2
print("\n" + "=" * 50)
print("TEST 3: Prediction - Extrovert Marketer")
print("=" * 50)
try:
    payload = {
        "interest": "marketing",
        "skills": ["copywriting", "social media"],
        "experience": "menengah",
        "personality": "extrovert"
    }
    response = requests.post(f"{API_URL}/predict", json=payload)
    data = response.json()
    if data['success']:
        print("✓ Prediction successful")
        for i, job in enumerate(data['jobs'], 1):
            print(f"\n  {i}. {job['title']}")
            print(f"     Score: {job['score']}%")
            print(f"     Skills to learn: {', '.join(job['skills_to_learn'][:2])}")
    else:
        print("✗ Error:", data.get('error'))
except Exception as e:
    print(f"✗ Error: {e}")

# Test 4: Predict with user input 3
print("\n" + "=" * 50)
print("TEST 4: Prediction - Tech-savvy Introvert")
print("=" * 50)
try:
    payload = {
        "interest": "teknologi",
        "skills": ["programming", "database"],
        "experience": "menengah",
        "personality": "introvert"
    }
    response = requests.post(f"{API_URL}/predict", json=payload)
    data = response.json()
    if data['success']:
        print("✓ Prediction successful")
        for i, job in enumerate(data['jobs'], 1):
            print(f"\n  {i}. {job['title']}")
            print(f"     Score: {job['score']}%")
    else:
        print("✗ Error:", data.get('error'))
except Exception as e:
    print(f"✗ Error: {e}")

# Test 5: Get history
print("\n" + "=" * 50)
print("TEST 5: Get History")
print("=" * 50)
try:
    response = requests.get(f"{API_URL}/history")
    data = response.json()
    if data['success']:
        print(f"✓ History retrieved successfully")
        print(f"  Total records: {len(data['history'])}")
        if data['history']:
            latest = data['history'][-1]
            print(f"  Latest prediction: {latest['interest']} -> {latest['results'][0]['title']}")
    else:
        print("✗ Error:", data.get('error'))
except Exception as e:
    print(f"✗ Error: {e}")

print("\n" + "=" * 50)
print("ALL TESTS COMPLETED")
print("=" * 50)
