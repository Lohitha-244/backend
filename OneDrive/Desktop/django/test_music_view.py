import os
import sys
import django
from django.test import RequestFactory
from rest_framework.test import force_authenticate

sys.path.append(r'c:\Users\kamat\OneDrive\Desktop\django\mentalhealth')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mentalhealth.settings')
django.setup()

from myapp.views import MusicTrackListAPIView
from django.contrib.auth import get_user_model

User = get_user_model()
user = User.objects.first() # Get any user for auth

def test_view(mood):
    print(f"\n--- Testing mood: '{mood}' ---")
    factory = RequestFactory()
    request = factory.get('/api/music/tracks/', {'mood': mood, 'category': 'music'})
    force_authenticate(request, user=user)
    
    view = MusicTrackListAPIView.as_view()
    response = view(request)
    
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.data
        print(f"Tracks returned: {len(data)}")
        for t in data:
            print(f" - ID {t['id']}: {t['title']} (Mood: {t['mood']})")
    else:
        print(f"Error data: {response.data}")

test_view("Calm")
test_view("calm")
test_view("Meditative")
test_view("meditative")
