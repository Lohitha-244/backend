import os
import sys
import django

sys.path.append(r'c:\Users\kamat\OneDrive\Desktop\django\mentalhealth')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mentalhealth.settings')
django.setup()

from myapp.models import MusicTrack
tracks = MusicTrack.objects.all()
for t in tracks:
    audio_val = t.audio.url if t.audio else (t.audio_url if t.audio_url else "None")
    print(f"{t.id}|{t.mood}|{t.category}|{t.is_active}|{audio_val}")
