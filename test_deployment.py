import requests
import json

# Test API endpoints
base_url = 'https://smart-career-production.up.railway.app'

print('🔍 Testing Railway deployment...')

# Test root endpoint
try:
    response = requests.get(base_url, timeout=10)
    print(f'✅ Root endpoint: {response.status_code}')
    if response.status_code == 200:
        print('   Frontend loads successfully!')
    else:
        print(f'   Response: {response.text[:200]}...')
except Exception as e:
    print(f'❌ Root endpoint failed: {e}')

# Test API options
try:
    response = requests.get(f'{base_url}/api/options', timeout=10)
    print(f'✅ API options: {response.status_code}')
    if response.status_code == 200:
        data = response.json()
        print(f'   Skills available: {len(data.get("skills", []))}')
        print(f'   Success: {data.get("success")}')
    else:
        print(f'   Response: {response.text[:200]}...')
except Exception as e:
    print(f'❌ API options failed: {e}')

# Test predict endpoint with sample data
try:
    test_data = {
        'interest': 'teknologi',
        'skills': ['programming', 'database'],
        'experience': 'menengah',
        'personality': 'introvert'
    }
    response = requests.post(f'{base_url}/predict',
                           json=test_data,
                           headers={'Content-Type': 'application/json'},
                           timeout=15)
    print(f'✅ Predict API: {response.status_code}')
    if response.status_code == 200:
        data = response.json()
        if data.get('success'):
            print(f'   Recommendations: {len(data.get("jobs", []))}')
            if data.get('jobs'):
                print(f'   Top job: {data["jobs"][0]["title"]}')
        else:
            print(f'   Error: {data.get("error", "Unknown")}')
    else:
        print(f'   Response: {response.text[:200]}...')
except Exception as e:
    print(f'❌ Predict API failed: {e}')

print('\n📋 Railway URL: https://smart-career-recommender-production.up.railway.app')
print('🌐 If issues persist, check Railway logs for detailed errors')