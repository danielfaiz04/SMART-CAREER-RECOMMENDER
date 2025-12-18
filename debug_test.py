import requests
import json
import time
import sys

print("Waiting for server to be ready...")
time.sleep(3)

print("\n" + "="*60)
print("TESTING /api/options ENDPOINT")
print("="*60)

try:
    print("\nSending GET request to http://localhost:5000/api/options...")
    response = requests.get('http://localhost:5000/api/options', timeout=10)
    print(f"Response received: Status Code {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"✓ SUCCESS!")
        print(f"  - Skills: {len(data.get('skills', []))} available")
        print(f"  - Interests: {data.get('interests', [])}")
        print(f"  - Experiences: {data.get('experiences', [])}")
        print(f"  - Personalities: {data.get('personalities', [])}")
    else:
        print(f"✗ Failed: {response.text}")
        
except requests.exceptions.ConnectionError as e:
    print(f"✗ Connection Error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"✗ Exception: {type(e).__name__}: {e}")
    sys.exit(1)

print("\n" + "="*60)
print("Test Complete!")
print("="*60)
