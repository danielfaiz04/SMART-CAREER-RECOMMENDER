import requests
import json
import time

time.sleep(2)

print("=" * 50)
print("SIMPLE API TEST")
print("=" * 50)

# Test 1: Options
print("\n1. Testing /api/options...")
try:
    r = requests.get('http://localhost:5000/api/options', timeout=5)
    print(f"   Status: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        print(f"   ✓ Success: {len(data['skills'])} skills available")
    else:
        print(f"   ✗ Error: {r.text}")
except Exception as e:
    print(f"   ✗ Exception: {e}")

# Test 2: Simple prediction
print("\n2. Testing /predict...")
try:
    payload = {
        "interest": "desain",
        "skills": ["design", "adobe"],
        "experience": "pemula",
        "personality": "introvert"
    }
    r = requests.post('http://localhost:5000/predict', json=payload, timeout=5)
    print(f"   Status: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        if data['success']:
            print(f"   ✓ Success: {len(data['jobs'])} recommendations")
            for job in data['jobs'][:3]:
                print(f"     - {job['title']}: {job['score']}%")
        else:
            print(f"   ✗ Error: {data.get('error')}")
    else:
        print(f"   ✗ Error: {r.text}")
except Exception as e:
    print(f"   ✗ Exception: {e}")

# Test 3: History
print("\n3. Testing /history...")
try:
    r = requests.get('http://localhost:5000/history', timeout=5)
    print(f"   Status: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        print(f"   ✓ Success: {len(data['history'])} history records")
    else:
        print(f"   ✗ Error: {r.text}")
except Exception as e:
    print(f"   ✗ Exception: {e}")

print("\n" + "=" * 50)
print("ALL TESTS COMPLETED")
print("=" * 50)
