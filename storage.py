# storage.py
# ---------------------------------
# Global in-memory storage (simple dictionary)
# ---------------------------------

# Structure:
# user_data = {
#     user_id: {
#         "lang": "en" | "ru" | "uz",
#         "level": "A1" | "A2" | "B1" | "B2" | "C1"
#     }
# }

user_data = {}


# --------------------------
# LANGUAGE MANAGEMENT
# --------------------------

def set_user_lang(user_id: int, lang: str):
    """Store the selected language for the user."""
    user_id = int(user_id)
    if user_id not in user_data:
        user_data[user_id] = {}
    user_data[user_id]["lang"] = lang


def get_user_lang(user_id: int) -> str:
    """Return the user's saved language, default = 'en'."""
    user_id = int(user_id)
    entry = user_data.get(user_id)

    if not entry:
        return "en"

    return entry.get("lang", "en")


# --------------------------
# LEVEL MANAGEMENT
# --------------------------

def set_user_level(user_id: int, level: str):
    """Save the user's English level result."""
    user_id = int(user_id)
    if user_id not in user_data:
        user_data[user_id] = {}
    user_data[user_id]["level"] = level


def get_user_level(user_id: int):
    """Get the saved level or return None if user has no level yet."""
    user_id = int(user_id)
    entry = user_data.get(user_id)

    if not entry:
        return None

    return entry.get("level")
