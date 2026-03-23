import os
import sys
import django
from django.utils import timezone
from datetime import timedelta, datetime

sys.path.append(r'c:\Users\kamat\OneDrive\Desktop\django\mentalhealth')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mentalhealth.settings')
django.setup()

from myapp.models import MoodCheckIn
from django.contrib.auth import get_user_model

User = get_user_model()
user = User.objects.filter(username='lohi').first()

if user:
    today = timezone.localdate()
    start_week = today - timedelta(days=today.weekday())
    
    start_dt = timezone.make_aware(datetime.combine(start_week, datetime.min.time()))
    
    print(f"User: {user.username}")
    print(f"Today: {today}")
    print(f"Start Week Date: {start_week}")
    print(f"Start Week DT: {start_dt}")
    
    count_date = MoodCheckIn.objects.filter(user=user, created_at__date__gte=start_week).count()
    count_gte = MoodCheckIn.objects.filter(user=user, created_at__gte=start_dt).count()
    
    print(f"Count with __date__gte: {count_date}")
    print(f"Count with __gte (DT): {count_gte}")
    
    # Check all records for this user today
    all_today = MoodCheckIn.objects.filter(user=user, created_at__date=today)
    print(f"Count exact today with __date: {all_today.count()}")
else:
    print("User 'lohi' not found")
