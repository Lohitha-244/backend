import os
import sys
import django
from django.utils import timezone
from datetime import timedelta

sys.path.append(r'c:\Users\kamat\OneDrive\Desktop\django\mentalhealth')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mentalhealth.settings')
django.setup()

from myapp.models import MoodCheckIn, JournalEntry, SoundPlay, BodyScanSession, MeditationSession, UserStats
from django.contrib.auth import get_user_model

User = get_user_model()
user = User.objects.first() # Let's check the first user as a proxy or find current user

def debug_user_activity(user):
    print(f"User: {user.username}")
    today = timezone.localdate()
    start_week = today - timedelta(days=today.weekday())
    start_month = today.replace(day=1)
    
    print(f"Today: {today}")
    print(f"Start of week: {start_week}")
    print(f"Start of month: {start_month}")
    
    models = [MoodCheckIn, JournalEntry, SoundPlay, BodyScanSession, MeditationSession]
    for model in models:
        total = model.objects.filter(user=user).count()
        this_week = 0
        if hasattr(model, 'created_at'):
            this_week = model.objects.filter(user=user, created_at__date__gte=start_week).count()
            latest = model.objects.filter(user=user).order_by('-created_at').first()
            latest_time = latest.created_at if latest else "None"
        elif hasattr(model, 'started_at'):
            this_week = model.objects.filter(user=user, started_at__date__gte=start_week).count()
            latest = model.objects.filter(user=user).order_by('-started_at').first()
            latest_time = latest.started_at if latest else "None"
        
        print(f"{model.__name__}: Total={total}, ThisWeek={this_week}, Latest={latest_time}")

for u in User.objects.all():
    debug_user_activity(u)
    print("-" * 20)
