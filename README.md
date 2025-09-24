# Discord Bot — Discord Community Developer

A modular Discord bot built in Python for **raid coordination** and **community management**. 
This repository is a **showcase** of the system I designed and implemented. It intentionally excludes the proprietary implementation to protect the project’s originality. 
You can **see it live** and interact with it here: **https://discord.gg/XMeevpkj**.

> ⚠️ Source code for the bot’s features is not displayed. This repo documents the design, capabilities, and structure.

## 👋 What this bot does (Feature Overview)
- **Country Selection (Voice/Text)** — Users pick their country to unlock region-specific voice/text channels and roles.
- **Verification** — Secure onboarding to keep the server clean from spam/bots.
- **Welcome & Leave** — Automated welcome messages, role hints, and clean leave logs.
- **Raid System** — Create, manage, and auto-close raid lobbies; balance groups dynamically.
- **Party Finder (Dungeons)** — Fast matchmaking flow to form dungeon parties with role preferences.
- **Gather** — Daily/periodic resource collection with inventory and cooldown logic.
- **Ticketing** — Private support channels for staff–user communication.
- **Level System** — XP and leveling to reward activity; cosmetic roles and milestones.
- **Giveaways** — Scheduled and one-off giveaways with fair winner selection.
- **Announcements** — Automated and manual announcements with scheduling support.
- **Raid × Availability** — Availability collection + raid scheduling; resolves conflicts.
- **Rates** — Configurable rate tables (e.g., drop rates/boosts/modifiers) surfaced to users.
- **Calendar** — Server calendar for events/raids; reminders and iCal-style logic.
- **Radio 24/7** — Continuous audio streaming in a designated voice channel.

➡️ **Join the Discord** to see these features in action: https://discord.gg/XMeevpkj

## 🧭 Channel Map (How the server is organized)
- `#welcome` — Onboarding, rules, and verification entry point.
- `#choose-your-country` — Pick country (reaction/menu); unlocks regional channels.
- `#announcements` — Global news, raid timelines, winners.
- `#raid-lobby` — Create/join raids; bot manages capacity and auto-closes.
- `#party-finder` — Quick dungeon party formation (role-based).
- `#gather` — Use gather commands and track resources.
- `#giveaways` — Participate in giveaways and view results.
- `#tickets` — Open private support requests for staff.
- `#levels` — Level/XP info and milestones.
- `#calendar` — Upcoming events and raid schedules.
- `#radio-247` — 24/7 music/radio voice channel controlled via text commands.

## 🧩 Technical architecture (high level)
- **Language & Framework**: Python, discord.py
- **Modularity**: Cog-based architecture; each feature is an extension.
- **Persistence**: SQLite/JSON for lightweight storage and portability.
- **Schedulers**: Timers and recurring tasks for events, reminders, and announcements.
- **Safety**: Token and secrets are injected via environment variables; sensitive code remains private.
- **Scalability**: Features can be toggled on/off per guild; state isolation per server.

## ✅ Prerequisites

- **Python**: 3.11+ (works on 3.10–3.12).  

- **Dependencies**:
  - Install from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
  - Includes: `discord.py[voice]`, `apscheduler`, `pytz`, `python-dotenv`, `aiosqlite`, `PyNaCl`.

- **Discord Application & Bot** (via [Discord Developer Portal](https://discord.com/developers/applications)):
  - Create an application → add a **Bot** → copy the **token** and store it safely.
  - **OAuth2 scopes** when inviting: `bot`, `applications.commands`.
  - **Recommended permissions**: 
    - Send Messages  
    - Read Message History  
    - Manage Messages  
    - Embed Links  
    - Attach Files  
    - Add Reactions  
    - Use Slash Commands  
    - (Optional) Manage Roles / Manage Channels (for role assignment, country channels)  
    - (Optional) Connect / Speak (for Radio 24/7)  
  - **Gateway Intents** (enable under *Bot → Privileged Gateway Intents*):
    - ✅ Server Members (needed for verification and role assignment)  
    - ✅ Message Content (only if parsing raw messages; not needed for slash commands)  
    - ✅ Presence (optional)  
    - ✅ Guilds & Voice States (for voice and radio features)  

- **System tools (for Radio 24/7 + voice features)**:
  - [FFmpeg](https://ffmpeg.org/download.html) (required).  
    - Windows: download FFmpeg and add it to PATH.  
    - Linux (Debian/Ubuntu): `sudo apt install ffmpeg`
  - **Opus codec** (usually bundled).  
    - Linux: `sudo apt install libopus0`

- **Storage**: SQLite (bundled with Python).  
  - Ensure the app has write permissions for the `data/` directory.  

- **Environment variables / settings**:
  - `DISCORD_BOT_TOKEN`.  
  - Optional: `TIMEZONE` for calendars and schedulers.  

- **Hosting** (for production or 24/7 uptime):  
  - VPS/VM or Docker setup with a process manager (e.g., `systemd`, `pm2`, or `docker compose`).  
  - NTP time sync recommended for accurate scheduling.

## 🔒 Why the implementation is private
- Prevent idea and approach cloning while I continue to iterate.
- Maintain a competitive edge while demonstrating my engineering rigor and design thinking.

## 📦 What’s included in this repo
- This **README** (overview and documentation).
- `/docs/FEATURES.md` — Deeper descriptions and flows for each feature and better undrstanding for anyone interested.
- `/docs/CHANNELS.md` — Server layout and behavior of each channel.
- `settings.example.py` — A **safe** template of configuration keys.
- `requirements.txt` — High-level dependency list (no private libs).
- `.gitignore` —.

## 🚀 See it live
Best way to evaluate: interact with the running bot in the community server.  
👉 **https://discord.gg/XMeevpkj**

## 👤 Author
**Ioannis Kaldiris** — Java & Python developer, with a focus on backend systems, Discord integrations, and scalable architectures.  
Explore more of my work: https://github.com/IoannisKaldiris


<p align="center">
  <a href="https://www.python.org/downloads/">
    <img alt="Python" src="https://img.shields.io/badge/Python-3.11%2B-blue">
  </a>
  <a href="https://discordpy.readthedocs.io/en/stable/">
    <img alt="discord.py" src="https://img.shields.io/badge/discord.py-2.x-informational">
  </a>
  <a href="LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-green">
  </a>
  <a href="https://discord.gg/XMeevpkj">
    <img alt="Status" src="https://img.shields.io/badge/Live-Bot%20in%20Discord-brightgreen">
  </a>
</p>
