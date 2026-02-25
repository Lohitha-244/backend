import re
from rest_framework import serializers

SPECIALS = r"""!@#$%^&*(),.?":{}|<>"""

def validate_password_strength(password: str) -> str:
    if len(password) < 6:
        raise serializers.ValidationError("Password must be at least 6 characters.")
    if not re.search(r"[A-Z]", password):
        raise serializers.ValidationError("Password must contain at least one uppercase letter.")
    if not re.search(r"[0-9]", password):
        raise serializers.ValidationError("Password must contain at least one number.")
    if not re.search(rf"[{re.escape(SPECIALS)}]", password):
        raise serializers.ValidationError("Password must contain at least one special character.")
    return password