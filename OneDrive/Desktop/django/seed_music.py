import os
import sys
import django

sys.path.append(r'c:\Users\kamat\OneDrive\Desktop\django\mentalhealth')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mentalhealth.settings')
django.setup()

from myapp.models import MusicTrack

def seed_tracks():
    moods = ["calm", "peace", "happy", "focus", "energize", "sleep", "meditative"]
    
    # Optional: clear existing music tracks to avoid confusion
    # MusicTrack.objects.filter(category="music").delete()
    
    for mood in moods:
        # Check if 2 tracks already exist
        existing = MusicTrack.objects.filter(mood=mood, category="music").count()
        if existing < 2:
            for i in range(existing, 2):
                MusicTrack.objects.create(
                    title=f"{mood.capitalize()} Track {i+1}",
                    mood=mood,
                    category="music",
                    description=f"Soothing {mood} soundscape for relaxation.",
                    is_active=True,
                    duration_seconds=300
                )
                print(f"Created {mood} track {i+1}")

seed_tracks()
