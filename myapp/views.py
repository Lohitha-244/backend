import random
from .ai import generate_reply
from .models import ChatSession, ChatMessage
from .serializers import ChatSendSerializer
from django.conf import settings
from django.core.mail import send_mail
from datetime import date
from django.contrib.auth.models import User
from datetime import timedelta
from rest_framework import status, permissions

from .models import PasswordResetOTP
from .validators import validate_password_strength

from .models import UserProfile, PasswordResetOTP
from .serializers import (
    RegisterSerializer,
    ProfileSerializer,
    ForgotPasswordSerializer,
    VerifyOTPSerializer,
    ResetPasswordSerializer,
)

from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import UserStats, DailyMotivationQuote
from .serializers import HomeSummarySerializer


# =========================
# REGISTER
# =========================
class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.save()
        UserProfile.objects.get_or_create(user=user)

        return Response({"message": "Account created successfully."}, status=status.HTTP_201_CREATED)


# =========================
# PROFILE
# =========================
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile, _ = UserProfile.objects.get_or_create(user=request.user)
        return Response(ProfileSerializer(profile).data, status=status.HTTP_200_OK)

    def put(self, request):
        profile, _ = UserProfile.objects.get_or_create(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


# =========================
# FORGOT PASSWORD (SEND OTP)
# =========================
class ForgotPasswordView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data["email"].lower().strip()

        if not User.objects.filter(email=email).exists():
            return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)

        otp = str(random.randint(100000, 999999))
        PasswordResetOTP.objects.create(email=email, otp=otp)

        try:
            send_mail(
                subject="Your Password Reset OTP",
                message=f"Your OTP is {otp}. It expires in 5 minutes.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
        except Exception as e:
            return Response(
                {"error": "Email failed to send", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response({"message": "OTP sent successfully"}, status=status.HTTP_200_OK)


# =========================
# VERIFY OTP (ISSUE reset_token)
# =========================



class VerifyOTPView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get("email", "").lower().strip()
        otp = request.data.get("otp", "").strip()

        if not email or not otp:
            return Response({"error": "email and otp are required"}, status=status.HTTP_400_BAD_REQUEST)

        otp_obj = PasswordResetOTP.objects.filter(email=email, otp=otp).order_by("-created_at").first()
        if not otp_obj:
            return Response({"error": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)

        # 5 min expiry
        if otp_obj.otp_is_expired():
            return Response({"error": "OTP expired"}, status=status.HTTP_400_BAD_REQUEST)

        # issue reset token (valid for 10 min)
        otp_obj.is_verified = True
        reset_token = otp_obj.issue_reset_token()

        return Response(
            {"message": "OTP verified successfully", "reset_token": str(reset_token)},
            status=status.HTTP_200_OK
        )


class ResetPasswordView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get("email", "").lower().strip()
        reset_token = request.data.get("reset_token", "").strip()
        new_password = request.data.get("new_password", "")

        if not email or not reset_token or not new_password:
            return Response(
                {"error": "email, reset_token and new_password are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # ✅ enforce strong password in backend also
        validate_password_strength(new_password)

        otp_obj = PasswordResetOTP.objects.filter(
            email=email,
            reset_token=reset_token,
            is_verified=True
        ).order_by("-reset_token_created_at").first()

        if not otp_obj:
            return Response({"error": "Invalid reset token"}, status=status.HTTP_400_BAD_REQUEST)

        if otp_obj.token_is_expired():
            return Response({"error": "Reset token expired"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()

        # optional: invalidate token after reset
        otp_obj.reset_token = None
        otp_obj.reset_token_created_at = None
        otp_obj.is_verified = False
        otp_obj.save(update_fields=["reset_token", "reset_token_created_at", "is_verified"])

        return Response({"message": "Password reset successful"}, status=status.HTTP_200_OK)
    



from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated

class HomeSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today_str = timezone.localdate().strftime("%A, %B %d")

        data = {
            "username": request.user.username,
            "date": today_str,
            "level": 1,
            "streak_days": 0,
            "coins": 0,
            "xp_progress": 0,
            "xp_total": 100,
            "daily_motivation": "Your speed doesn't matter, forward is forward."
        }
        return Response(data, status=status.HTTP_200_OK)
    




def is_crisis_message(text: str) -> bool:
    t = (text or "").lower()
    crisis_keywords = [
        "suicide", "kill myself", "end my life", "self harm", "self-harm",
        "cut myself", "die", "no reason to live"
    ]
    return any(k in t for k in crisis_keywords)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .models import ChatSession, ChatMessage
from .serializers import ChatSendSerializer
from .ai import generate_reply


class ChatbotSendView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ChatSendSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user_message = serializer.validated_data["message"].strip()

        # Get or create session
        session, _ = ChatSession.objects.get_or_create(
            user=request.user,
            defaults={"title": "AI Wellness Chat"}
        )

        # Save user message
        ChatMessage.objects.create(session=session, role="user", content=user_message)

        # Fetch last 12 messages (includes the just-saved user message)
        recent_msgs = ChatMessage.objects.filter(session=session).order_by("-created_at")[:12]
        recent_msgs = list(reversed(recent_msgs))

        # ✅ Remove the last message if it's the same user_message (avoid duplicate in OpenAI messages)
        if recent_msgs and recent_msgs[-1].role == "user" and recent_msgs[-1].content == user_message:
            recent_msgs = recent_msgs[:-1]

        # Build history for OpenAI
        history = [
            {"role": m.role, "content": m.content}
            for m in recent_msgs
            if m.role in ("user", "assistant")
        ]

        # ✅ Generate dynamic reply (OpenAI / crisis handled in ai.py)
        reply = generate_reply(user_message=user_message, history=history)

        # Save assistant reply
        ChatMessage.objects.create(session=session, role="assistant", content=reply)

        return Response({"reply": reply}, status=status.HTTP_200_OK)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .models import ChatSession
from .serializers import ChatSessionSerializer


class ChatHistoryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        session = ChatSession.objects.filter(user=request.user).order_by("-created_at").first()
        if not session:
            return Response({"messages": []}, status=status.HTTP_200_OK)

        return Response(ChatSessionSerializer(session).data, status=status.HTTP_200_OK)
    

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404

from .models import MoodSession, MoodQuestion, MoodAnswer
from .serializers import (
    MoodStartSerializer,
    MoodAnswerSerializer,
    MoodQuestionSerializer,
    MoodSessionHistorySerializer
)

def _get_total_questions(mood: str) -> int:
    return MoodQuestion.objects.filter(mood=mood).count()

def _get_next_question(session: MoodSession):
    answered_ids = MoodAnswer.objects.filter(session=session).values_list("question_id", flat=True)
    return MoodQuestion.objects.filter(mood=session.mood).exclude(id__in=answered_ids).order_by("order").first()

class MoodStartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        ser = MoodStartSerializer(data=request.data)
        if not ser.is_valid():
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

        mood = ser.validated_data["mood"].lower().strip()
        stress_level = ser.validated_data["stress_level"]

        session = MoodSession.objects.create(
            user=request.user,
            mood=mood,
            stress_level=stress_level
        )

        q = _get_next_question(session)
        total = _get_total_questions(mood)

        if not q:
            session.is_completed = True
            session.save(update_fields=["is_completed"])
            return Response(
                {"message": "No questions configured for this mood yet.", "session_id": session.id},
                status=status.HTTP_200_OK
            )

        answered_count = 0
        return Response({
            "session_id": session.id,
            "question": MoodQuestionSerializer(q).data,
            "progress": {"current": answered_count + 1, "total": total}
        }, status=status.HTTP_200_OK)

class MoodAnswerView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        ser = MoodAnswerSerializer(data=request.data)
        if not ser.is_valid():
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

        session = get_object_or_404(MoodSession, id=ser.validated_data["session_id"], user=request.user)
        question = get_object_or_404(MoodQuestion, id=ser.validated_data["question_id"], mood=session.mood)

        MoodAnswer.objects.update_or_create(
            session=session,
            question=question,
            defaults={"answer_text": ser.validated_data.get("answer_text", "")}
        )

        next_q = _get_next_question(session)
        total = _get_total_questions(session.mood)
        answered_count = MoodAnswer.objects.filter(session=session).count()

        if not next_q:
            session.is_completed = True
            session.save(update_fields=["is_completed"])
            return Response({"message": "Mood check-in completed", "session_id": session.id}, status=status.HTTP_200_OK)

        return Response({
            "question": MoodQuestionSerializer(next_q).data,
            "progress": {"current": answered_count + 1, "total": total}
        }, status=status.HTTP_200_OK)

class MoodHistoryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        qs = MoodSession.objects.filter(user=request.user).order_by("-created_at")[:30]
        return Response(MoodSessionHistorySerializer(qs, many=True).data, status=status.HTTP_200_OK)
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .models import MoodQuestion, MoodOption, MoodCheckIn, MoodAnswer
from .serializers_mood import (
    MoodQuestionSerializer,
    MoodCheckInCreateSerializer,
    MoodCheckInReadSerializer,
)


class MoodQuestionsAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # GET /api/mood/questions/?mood=angry
    def get(self, request):
        mood = request.query_params.get("mood")
        if not mood:
            return Response({"detail": "mood is required"}, status=400)

        qs = MoodQuestion.objects.filter(mood=mood).prefetch_related("options")
        return Response(MoodQuestionSerializer(qs, many=True).data)


class MoodCheckInCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # POST /api/mood/checkin/
    # {
    #   "mood": "angry",
    #   "stress_level": 5,
    #   "answers": [
    #      {"question_id": 10, "option_id": 55},
    #      {"question_id": 11, "option_id": 60},
    #      {"question_id": 12, "option_id": 62}
    #   ]
    # }
    def post(self, request):
        serializer = MoodCheckInCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mood = serializer.validated_data["mood"]
        stress_level = serializer.validated_data["stress_level"]
        answers = serializer.validated_data["answers"]

        checkin = MoodCheckIn.objects.create(
            user=request.user,
            mood=mood,
            stress_level=stress_level,
        )

        for a in answers:
            qid = a["question_id"]
            opt_id = a.get("option_id")
            answer_text = a.get("answer_text", "")

            question = MoodQuestion.objects.get(id=qid, mood=mood)

            selected_option = None
            if opt_id:
                selected_option = MoodOption.objects.get(id=opt_id, question=question)

            MoodAnswer.objects.create(
                checkin=checkin,
                question=question,
                selected_option=selected_option,
                answer_text=answer_text,
            )

        return Response(MoodCheckInReadSerializer(checkin).data, status=status.HTTP_201_CREATED)


class MoodCheckInHistoryAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # GET /api/mood/history/
    def get(self, request):
        qs = (
            MoodCheckIn.objects.filter(user=request.user)
            .prefetch_related("answers__question", "answers__selected_option")
            .order_by("-created_at")[:50]
        )
        return Response(MoodCheckInReadSerializer(qs, many=True).data)