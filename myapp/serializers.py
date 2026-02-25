from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile
from .validators import validate_password_strength
from .models import UserStats
from django.utils import timezone
from .models import ChatSession, ChatMessage
from .models import MoodSession, MoodQuestion, MoodAnswer
# =========================
# REGISTER
# =========================
class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def validate_password(self, value):
        return validate_password_strength(value)

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data["email"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


# =========================
# PROFILE
# =========================
class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = UserProfile
        fields = ["username", "email"]

# =========================
# FORGOT PASSWORD
# =========================
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


# =========================
# VERIFY OTP
# =========================
class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)


# =========================
# RESET PASSWORD
# =========================
class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    reset_token = serializers.UUIDField()
    new_password = serializers.CharField(write_only=True)

    def validate_new_password(self, value):
        return validate_password_strength(value)


class HomeSummarySerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    daily_quote = serializers.SerializerMethodField()

    class Meta:
        model = UserStats
        fields = [
            "date",
            "level",
            "streak_days",
            "coins",
            "xp_current",
            "xp_target",
            "daily_quote",
        ]

    def get_date(self, obj):
        return timezone.localdate().isoformat()

    def get_daily_quote(self, obj):
        return obj.daily_quote.text if obj.daily_quote else "Stay strong. You’re doing great."
    

class ChatSendSerializer(serializers.Serializer):
    message = serializers.CharField()
    session_id = serializers.IntegerField(required=False)

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ["id", "role", "content", "created_at"]

class ChatSessionSerializer(serializers.ModelSerializer):
    messages = ChatMessageSerializer(many=True, read_only=True)

    class Meta:
        model = ChatSession
        fields = ["id", "title", "created_at", "messages"]
        from rest_framework import serializers

class ChatSendSerializer(serializers.Serializer):
    message = serializers.CharField()
    session_id = serializers.IntegerField(required=False)
class ChatSendSerializer(serializers.Serializer):
    message = serializers.CharField()

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ["id", "role", "content", "created_at"]

class ChatSessionSerializer(serializers.ModelSerializer):
    messages = ChatMessageSerializer(many=True, read_only=True)

    class Meta:
        model = ChatSession
        fields = ["id", "title", "created_at", "messages"]

class MoodStartSerializer(serializers.Serializer):
    mood = serializers.CharField()
    stress_level = serializers.IntegerField(min_value=1, max_value=10)

class MoodQuestionSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="qtype")

    class Meta:
        model = MoodQuestion
        fields = ["id", "text", "type", "options"]

class MoodAnswerSerializer(serializers.Serializer):
    session_id = serializers.IntegerField()
    question_id = serializers.IntegerField()
    answer_text = serializers.CharField(allow_blank=True, required=False, default="")

class MoodSessionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodSession
        fields = ["id", "mood", "stress_level", "created_at", "is_completed"]





from rest_framework import serializers
from .models import MoodQuestion, MoodOption, MoodCheckIn, MoodAnswer


class MoodOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodOption
        fields = ["id", "text"]


class MoodQuestionSerializer(serializers.ModelSerializer):
    options = MoodOptionSerializer(many=True, read_only=True)

    class Meta:
        model = MoodQuestion
        fields = ["id", "mood", "order", "text", "options"]


class MoodAnswerWriteSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    option_id = serializers.IntegerField(required=False)
    answer_text = serializers.CharField(required=False, allow_blank=True)


class MoodCheckInCreateSerializer(serializers.Serializer):
    mood = serializers.ChoiceField(choices=["great", "angry", "tired", "stressed", "sad"])
    stress_level = serializers.IntegerField(min_value=0, max_value=10)
    answers = MoodAnswerWriteSerializer(many=True)

    def validate(self, attrs):
        mood = attrs["mood"]
        qs = MoodQuestion.objects.filter(mood=mood)
        if qs.count() == 0:
            raise serializers.ValidationError("Questions not configured for this mood.")
        return attrs


class MoodAnswerReadSerializer(serializers.ModelSerializer):
    question_text = serializers.CharField(source="question.text", read_only=True)
    question_order = serializers.IntegerField(source="question.order", read_only=True)
    option_text = serializers.CharField(source="selected_option.text", read_only=True)

    class Meta:
        model = MoodAnswer
        fields = ["question_order", "question_text", "option_text", "answer_text"]


class MoodCheckInReadSerializer(serializers.ModelSerializer):
    answers = MoodAnswerReadSerializer(many=True, read_only=True)

    class Meta:
        model = MoodCheckIn
        fields = ["id", "mood", "stress_level", "created_at", "answers"]