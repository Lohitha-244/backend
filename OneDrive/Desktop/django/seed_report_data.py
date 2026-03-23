import os
import django
import sys
from django.utils import timezone
from datetime import timedelta
import random

# Set up Django environment
sys.path.append(r'c:\Users\kamat\OneDrive\Desktop\django\mentalhealth')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mentalhealth.settings')
django.setup()

from django.contrib.auth import get_user_model
from myapp.models import (
    MoodCheckIn, JournalEntry, GratitudeEntry, CreativeDrawing, 
    ChatSession, SoundPlay, BodyScanSession, MeditationSession,
    UserStats, UserAffirmationState, MusicTrack, MeditationProgram
)

User = get_user_model()

def seed_data_for_user(username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        print(f"User {username} not found. Skipping.")
        return

    print(f"Seeding data for {username}...")
    
    now = timezone.now()
    # Seed for the last 10 days to cover both week and month
    for i in range(10):
        date = now - timedelta(days=i)
        
        # 1. Mood Check-in
        MoodCheckIn.objects.create(
            user=user,
            mood=random.choice(["great", "okay", "tired", "stressed", "sad"]),
            stress_level=random.randint(1, 10),
            created_at=date
        )
        
        # 2. Journal Entry (every other day)
        if i % 2 == 0:
            JournalEntry.objects.create(
                user=user,
                text=f"Journal entry for {date.date()}: Feeling productive today.",
                created_at=date
            )
            
        # 3. Meditation Session (every day)
        program = MeditationProgram.objects.first()
        if program:
            MeditationSession.objects.create(
                user=user,
                program=program,
                started_at=date - timedelta(minutes=10),
                ended_at=date,
                duration_seconds=600,
                is_completed=True
            )
            
        # 4. Sound Play
        track = MusicTrack.objects.first()
        if track:
            SoundPlay.objects.create(
                user=user,
                track=track,
                started_at=date - timedelta(minutes=15),
                ended_at=date - timedelta(minutes=10),
                duration_seconds=300
            )

    print(f"Successfully seeded data for {username}.")

if __name__ == "__main__":
    # Seed for common users
    for uname in ['agent1', 'admin', 'lohitha@gmail.com']:
        seed_data_for_user(uname)
