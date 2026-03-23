import re
from django.conf import settings
from groq import Groq
from groq import APIConnectionError, BadRequestError, AuthenticationError

CRISIS_PATTERNS = [
    r"\bkill myself\b",
    r"\bsuicide\b",
    r"\bend my life\b",
    r"\bself[- ]harm\b",
    r"\bhurt myself\b",
]

def is_crisis(text: str) -> bool:
    t = (text or "").lower()
    return any(re.search(p, t) for p in CRISIS_PATTERNS)

CRISIS_REPLY = (
    "I’m really sorry you’re feeling this way. You don’t have to handle this alone.\n\n"
    "If you feel you might hurt yourself or you’re in immediate danger, please call your local emergency number now.\n"
    "In India, you can call 112 (emergency). You can also reach AASRA at 91-22-27546669.\n\n"
    "If you can, tell me: are you safe right now?"
)

SYSTEM_PROMPT = (
    "You are a calm, supportive mental wellness companion. "
    "Respond with empathy and validation. "
    "Ask one short follow-up question. "
    "Do not diagnose medical conditions."
)

def generate_reply(user_message: str, history: list[dict]) -> str:
    if is_crisis(user_message):
        return CRISIS_REPLY

    api_key = getattr(settings, "GROQ_API_KEY", None)
    if not api_key:
        return "Groq API key not configured. Set GROQ_API_KEY in .env"

    model = getattr(settings, "GROQ_MODEL", "llama-3.1-8b-instant")

    try:
        client = Groq(api_key=api_key)

        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        messages += history
        messages.append({"role": "user", "content": user_message})

        resp = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.6,
            max_tokens=200,
        )
        return resp.choices[0].message.content.strip()

    except BadRequestError as e:
        return f"Groq model error. Check GROQ_MODEL. Details: {e}"
    except AuthenticationError:
        return "Groq API key is invalid. Regenerate key in Groq Console and update .env"
    except APIConnectionError:
        return "Cannot reach Groq API (internet/DNS issue). Try hotspot or change network."
    except Exception as e:
        return f"AI error: {str(e)}"