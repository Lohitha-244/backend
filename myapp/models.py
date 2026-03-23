from datetime import timedelta
import uuid

from django.db import models
from django.utils import timezone
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL


class UserProfile(models.Model):
    user = models.OneToOneField(USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=20, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.user)


class PasswordResetOTP(models.Model):
    email = models.EmailField(db_index=True)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    is_verified = models.BooleanField(default=False)
    reset_token = models.UUIDField(null=True, blank=True)
    reset_token_created_at = models.DateTimeField(null=True, blank=True)

    def otp_is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=5)

    def token_is_expired(self):
        if not self.reset_token_created_at:
            return True
        return timezone.now() > self.reset_token_created_at + timedelta(minutes=10)

    def issue_reset_token(self):
        self.reset_token = uuid.uuid4()
        self.reset_token_created_at = timezone.now()
        self.save(update_fields=["reset_token", "reset_token_created_at"])
        return self.reset_token


class DailyMotivationQuote(models.Model):
    text = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.text[:50]


class UserStats(models.Model):
    user = models.OneToOneField(USER_MODEL, on_delete=models.CASCADE, related_name="stats")

    level = models.PositiveIntegerField(default=1)
    coins = models.PositiveIntegerField(default=0)

    xp_current = models.PositiveIntegerField(default=0)
    xp_target = models.PositiveIntegerField(default=100)

    streak_days = models.PositiveIntegerField(default=0)
    last_streak_date = models.DateField(null=True, blank=True)

    daily_quote = models.ForeignKey(
        DailyMotivationQuote, null=True, blank=True, on_delete=models.SET_NULL
    )
    daily_quote_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} stats"


class ChatSession(models.Model):
    user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE, related_name="chat_sessions")
    title = models.CharField(max_length=120, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.created_at}"


class ChatMessage(models.Model):
    ROLE_CHOICES = (("user", "user"), ("assistant", "assistant"))
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name="messages")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


# -------------------- MOOD CHECK-IN MODELS (ONE SET ONLY) --------------------

class Mood(models.TextChoices):
    GREAT = "great", "Great"
    ANGRY = "angry", "Angry"
    TIRED = "tired", "Tired"
    STRESSED = "stressed", "Stressed"
    SAD = "sad", "Sad"


class MoodSession(models.Model):
    """
    Optional session table (you already migrated it in 0007).
    Keep it to avoid schema mismatch.
    """
    user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    mood = models.CharField(max_length=20, choices=Mood.choices)
    stress_level = models.PositiveSmallIntegerField(default=0)  # 0..10
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} {self.mood} {self.created_at}"


class MoodQuestion(models.Model):
    mood = models.CharField(max_length=20, choices=Mood.choices)
    order = models.PositiveSmallIntegerField()  # 1,2,3...
    text = models.CharField(max_length=255)

    class Meta:
        unique_together = ("mood", "order")
        ordering = ["mood", "order"]

    def __str__(self):
        return f"{self.mood} Q{self.order}: {self.text}"


class MoodOption(models.Model):
    question = models.ForeignKey(MoodQuestion, on_delete=models.CASCADE, related_name="options")
    text = models.CharField(max_length=120)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.text


class MoodCheckIn(models.Model):
    user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE, related_name="mood_checkins")
    mood = models.CharField(max_length=20, choices=Mood.choices)
    stress_level = models.PositiveSmallIntegerField(default=0)  # 0..10
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.mood} {self.created_at}"


class MoodAnswer(models.Model):
    checkin = models.ForeignKey(MoodCheckIn, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(MoodQuestion, on_delete=models.PROTECT)
    selected_option = models.ForeignKey(MoodOption, null=True, blank=True, on_delete=models.SET_NULL)
    answer_text = models.CharField(max_length=255, blank=True, default="")

    class Meta:
        unique_together = ("checkin", "question")

    def __str__(self):
        return f"{self.checkin_id} - {self.question_id}"