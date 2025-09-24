# settings.example.py
# Copy to settings.py and fill in your own values.
# Do NOT commit the real settings.py.

DISCORD_BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
DEFAULT_PREFIX = "!"

# Core channels (by ID preferred)
CHANNELS = {
    "welcome": 0,
    "choose_country": 0,
    "announcements": 0,
    "raid_lobby": 0,
    "party_finder": 0,
    "gather": 0,
    "giveaways": 0,
    "tickets": 0,
    "levels": 0,
    "calendar": 0,
    "radio_247": 0,
}

# Feature toggles
FEATURES = {
    "verification": True,
    "welcome_leave": True,
    "raid": True,
    "party_finder": True,
    "gather": True,
    "tickets": True,
    "level_system": True,
    "giveaways": True,
    "announcements": True,
    "raid_availability": True,
    "rates": True,
    "calendar": True,
    "radio_247": True,
}

# Time zone, locales, etc.
TIMEZONE = "UTC"
LOCALE = "en-US"
