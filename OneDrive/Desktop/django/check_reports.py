import os
import django
import sys
from django.utils import timezone
from datetime import timedelta

# Set up Django environment
sys.path.append(r'c:\Users\kamat\OneDrive\Desktop\django\mentalhealth')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mentalhealth.settings')
django.setup()

from django.contrib.auth import get_user_model
from myapp.models import (
    MoodCheckIn, JournalEntry, GratitudeEntry, CreativeDrawing, 
    ChatSession, SoundPlay, BodyScanSession, MeditationSession,
    UserStats, UserAffirmationState
)
from myapp.views import _week_range, _month_range

User = get_user_model()

def check_user_reports(username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = User.objects.first()
        if not user:
            print("No users found.")
            return
        print(f"User {username} not found, using {user.username}")

    print(f"--- Report Diagnostics for User: {user.username} ---")
    
    # Weekly Range
    w_start, w_end = _week_range()
    print(f"Weekly Range: {w_start} to {w_end}")
    
    moods = MoodCheckIn.objects.filter(user=user, created_at__gte=w_start, created_at__lt=w_end).count()
    journals = JournalEntry.objects.filter(user=user, created_at__gte=w_start, created_at__lt=w_end).count()
    gratitudes = GratitudeEntry.objects.filter(user=user, created_at__gte=w_start, created_at__lt=w_end).count()
    drawings = CreativeDrawing.objects.filter(user=user, created_at__gte=w_start, created_at__lt=w_end).count()
    chats = ChatSession.objects.filter(user=user, created_at__gte=w_start, created_at__lt=w_end).count()
    
    total_checkins = moods + journals + gratitudes + drawings + chats
    
    sound_sessions = SoundPlay.objects.filter(user=user, started_at__gte=w_start, started_at__lt=w_end).count()
    bodyscan_sessions = BodyScanSession.objects.filter(user=user, started_at__gte=w_start, started_at__lt=w_end, is_completed=True).count()
    program_sessions = MeditationSession.objects.filter(user=user, started_at__gte=w_start, started_at__lt=w_end, is_completed=True).count()
    
    meditation_sessions = sound_sessions + bodyscan_sessions + program_sessions
    
    print(f"Weekly Summary:")
    print(f"  Moods: {moods}")
    print(f"  Journals: {journals}")
    print(f"  Gratitudes: {gratitudes}")
    print(f"  Drawings: {drawings}")
    print(f"  Chats: {chats}")
    print(f"  TOTAL CHECKINS: {total_checkins}")
    print(f"  MEDITATION SESSIONS: {meditation_sessions}")
    
    # Monthly Range
    m_start, m_end = _month_range()
    print(f"\nMonthly Range: {m_start} to {m_end}")
    
    active_days_set = set()
    
    # Activity days
    active_days_set.update({timezone.localtime(o.created_at).date() for o in MoodCheckIn.objects.filter(user=user, created_at__gte=m_start, created_at__lt=m_end)})
    active_days_set.update({timezone.localtime(o.created_at).date() for o in JournalEntry.objects.filter(user=user, created_at__gte=m_start, created_at__lt=m_end)})
    active_days_set.update({timezone.localtime(o.started_at).date() for o in SoundPlay.objects.filter(user=user, started_at__gte=m_start, started_at__lt=m_end)})
    active_days_set.update({timezone.localtime(o.started_at).date() for o in BodyScanSession.objects.filter(user=user, started_at__gte=m_start, started_at__lt=m_end, is_completed=True)})
    active_days_set.update({timezone.localtime(o.started_at).date() for o in MeditationSession.objects.filter(user=user, started_at__gte=m_start, started_at__lt=m_end, is_completed=True)})
    active_days_set.update({timezone.localtime(o.created_at).date() for o in GratitudeEntry.objects.filter(user=user, created_at__gte=m_start, created_at__lt=m_end)})
    active_days_set.update({timezone.localtime(o.created_at).date() for o in CreativeDrawing.objects.filter(user=user, created_at__gte=m_start, created_at__lt=m_end)})
    active_days_set.update({timezone.localtime(o.created_at).date() for o in ChatSession.objects.filter(user=user, created_at__gte=m_start, created_at__lt=m_end)})
    active_days_set.update({timezone.localtime(o.last_viewed_at).date() for o in UserAffirmationState.objects.filter(user=user, last_viewed_at__gte=m_start, last_viewed_at__lt=m_end)})
    
    print(f"\nAll-time Summary:")
    print(f"  Total Moods: {MoodCheckIn.objects.filter(user=user).count()}")
    print(f"  Total Journals: {JournalEntry.objects.filter(user=user).count()}")
    print(f"  Total Meditations (all types): {MeditationSession.objects.filter(user=user, is_completed=True).count() + SoundPlay.objects.filter(user=user).count() + BodyScanSession.objects.filter(user=user, is_completed=True).count()}")

if __name__ == "__main__":
    check_user_reports("agent1")
