import os
import sys
import django

sys.path.append(r'c:\Users\kamat\OneDrive\Desktop\django\mentalhealth')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mentalhealth.settings')
django.setup()

from myapp.models import MusicTrack

def cleanup_tracks():
    moods = ["calm", "peace", "happy", "focus", "energize", "sleep", "meditative"]
    for mood in moods:
        tracks = MusicTrack.objects.filter(mood=mood, category="music").order_by("id")
        count = tracks.count()
        if count > 1:
            # Delete all but the first one
            to_delete = tracks[1:]
            for t in to_delete:
                t.delete()
            print(f"Cleaned up {count - 1} extra tracks for {mood}")
        elif count == 0:
            # Create one if missing
            MusicTrack.objects.create(
                title=f"{mood.capitalize()} Soundscape",
                mood=mood,
                category="music",
                description=f"A unique {mood} audio experience.",
                is_active=True,
                duration_seconds=300
            )
            print(f"Created missing track for {mood}")

cleanup_tracks()
