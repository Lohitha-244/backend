from django.urls import path
from .views import (
    RegisterView, ProfileView,
    ForgotPasswordView, VerifyOTPView, ResetPasswordView,
    HomeSummaryView, ChatbotSendView
)
from .views import ChatbotSendView
from .views import ChatbotSendView, ChatHistoryView
from .views import MoodStartView, MoodAnswerView, MoodHistoryView
from django.urls import path
from .views_mood import MoodQuestionsAPIView, MoodCheckInCreateAPIView, MoodCheckInHistoryAPIView

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),

    path("auth/forgot-password/", ForgotPasswordView.as_view(), name="forgot_password"),
    path("auth/verify-otp/", VerifyOTPView.as_view(), name="verify_otp"),
    path("auth/reset-password/", ResetPasswordView.as_view(), name="reset_password"),

    path("home/summary/", HomeSummaryView.as_view(), name="home_summary"),
    path("chat/send/", ChatbotSendView.as_view(), name="chat_send"),
    path("chat/history/", ChatHistoryView.as_view(), name="chat_history"),
    
]

urlpatterns += [
    path("mood/start/", MoodStartView.as_view()),
    path("mood/answer/", MoodAnswerView.as_view()),
    path("mood/history/", MoodHistoryView.as_view()),
]

urlpatterns = [
    path("mood/questions/", MoodQuestionsAPIView.as_view()),
    path("mood/checkin/", MoodCheckInCreateAPIView.as_view()),
    path("mood/history/", MoodCheckInHistoryAPIView.as_view()),
]