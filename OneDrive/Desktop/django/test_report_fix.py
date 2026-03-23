import os
import django
import sys
import json
from django.test import RequestFactory
from rest_framework.test import force_authenticate

# Set up Django environment
sys.path.append(r'c:\Users\kamat\OneDrive\Desktop\django\mentalhealth')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mentalhealth.settings')
django.setup()

from django.contrib.auth import get_user_model
from myapp.views import WeeklyReportAPIView, MonthlyReportAPIView

User = get_user_model()

def test_reports(username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        print(f"User {username} not found.")
        return

    factory = RequestFactory()
    
    # Test Weekly
    print(f"\n--- Testing Weekly Report for {username} ---")
    view = WeeklyReportAPIView.as_view()
    request = factory.get('/api/progress/weekly/')
    force_authenticate(request, user=user)
    response = view(request)
    print(f"Status: {response.status_code}")
    print(f"Data: {json.dumps(response.data, indent=2)}")
    
    # Test Monthly
    print(f"\n--- Testing Monthly Report for {username} ---")
    view = MonthlyReportAPIView.as_view()
    request = factory.get('/api/progress/monthly/')
    force_authenticate(request, user=user)
    response = view(request)
    print(f"Status: {response.status_code}")
    print(f"Data: {json.dumps(response.data, indent=2)}")

if __name__ == "__main__":
    test_reports("agent1")
