import requests
import json

# Replace with the actual tunnel URL or 127.0.0.1:8000
BASE_URL = "http://127.0.0.1:8000"

def test_music_tracks(mood):
    print(f"Testing mood: {mood}")
    url = f"{BASE_URL}/api/music/tracks/?mood={mood}&category=music"
    try:
        # Note: Needs authentication if I want to test the actual view
        # But I can check if it returns 200 or 401 first.
        # Actually, I should use the same user as the app.
        # Let's try without auth first to see if it even reaches the filter logic (it won't if protected)
        response = requests.get(url) 
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            tracks = response.json()
            print(f"Tracks found: {len(tracks)}")
            for t in tracks:
                print(f" - {t['id']}: {t['title']} ({t['mood']})")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Exception: {e}")

# Since the view is protected by IsAuthenticated, I need a token.
# I'll use a script that runs inside the Django environment to test the view logic directly.
