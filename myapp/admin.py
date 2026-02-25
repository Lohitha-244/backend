from django.contrib import admin
from .models import DailyMotivationQuote, UserStats

admin.site.register(DailyMotivationQuote)
admin.site.register(UserStats)
from .models import ChatSession, ChatMessage

admin.site.register(ChatSession)
admin.site.register(ChatMessage)

from .models import MoodQuestion, MoodOption, MoodCheckIn, MoodAnswer

admin.site.register(MoodQuestion)
admin.site.register(MoodOption)
admin.site.register(MoodCheckIn)
admin.site.register(MoodAnswer)
