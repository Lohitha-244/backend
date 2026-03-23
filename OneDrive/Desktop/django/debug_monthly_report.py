import os
import sys
import django
from django.utils import timezone
from datetime import timedelta, datetime

sys.path.append(r'c:\Users\kamat\OneDrive\Desktop\django\mentalhealth')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mentalhealth.settings')
django.setup()

from myapp.views import MonthlyReportAPIView
from rest_framework.test import APIRequestFactory, force_authenticate
from django.contrib.auth import get_user_model

User = get_user_model()
user = User.objects.filter(username='lohi').first()

if not user:
    user = User.objects.first()

if user:
    print(f"Testing MonthlyReportAPIView for user: {user.username}")
    factory = APIRequestFactory()
    view = MonthlyReportAPIView.as_view()
    
    request = factory.get('/api/progress/monthly/')
    force_authenticate(request, user=user)
    
    try:
        response = view(request)
        print(f"Status Code: {response.status_code}")
        print(f"Response Data: {response.data}")
    except Exception as e:
        print(f"Error calling view: {e}")
        import traceback
        traceback.print_exc()
else:
    print("No users found to test.")
