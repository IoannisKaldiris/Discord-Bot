# Feature Details

Below is a non-code deep dive into how users experience each capability and how the system is organized internally (at a conceptual level).

## Country Selection (Voice/Text)
- **User flow**: User picks a country → bot assigns a country role → regional text/voice channels unlock.
- **Concepts**: Reaction/Select menus, role assignment, permission gating.
- **Admin controls**: Country list, emojis/labels, auto-channel provisioning.

## Verification
- **User flow**: On join → prompt → challenge/acknowledgement → role granted if passed.
- **Concepts**: Anti-spam heuristics, cooldowns, rate limits.
- **Admin controls**: Verification method, retry limits, quarantine role.

## Welcome & Leave
- **User flow**: Personalized welcome with role hints; leave messages routed to staff logs.
- **Concepts**: Templates with variables, media support.
- **Admin controls**: Templates, timing, destination channels.

## Market
- **User flow**: Members browse `#market` for rules and examples, then post in `#want-to-buy` or `#want-to-sell` using a guided template. The bot validates required fields, timestamps the post, and (optionally) auto-expires or archives listings after a set period. Buyers and sellers can continue in a thread or DM.
- **Concepts**: Structured listing templates (WTB/WTS), cooldowns and anti-spam, optional tags (e.g., rarity/tier), soft moderation (auto-delete on expiry), and light analytics (e.g., volume per day).
- **Admin controls**: Edit templates and required fields, set posting cooldowns, define listing lifetime (days), choose allowed roles to post, enable/disable auto-threads, and configure moderation actions for expired or non-compliant posts.


## Raid System
- **User flow**: Create raid → define capacity → users join/leave → auto-close after timeout or full.
- **Concepts**: Lobby state machine, capacity management, role/priority filters.
- **Admin controls**: Default capacity, timeouts, leader rights, multi-raid concurrency.

## Party Finder (Dungeons)
- **User flow**: Open party → pick roles → bot matches players by role and readiness.
- **Concepts**: Role-based matching, queue management, ready-check.
- **Admin controls**: Role taxonomy, max team size, timeouts.

## Gather
- **User flow**: Periodic command to collect resources with cooldown; inventory tracking.
- **Concepts**: Cooldowns, pseudo-RNG yields, economy hooks.
- **Admin controls**: Drop tables, cooldown durations, rarity tiers.

## Ticketing
- **User flow**: Open ticket → private thread/chan with staff → resolve/close.
- **Concepts**: Permissioned channels/threads, transcripts.
- **Admin controls**: Categories, transcript export, SLA prompts.

## Level System
- **User flow**: Get XP on activity → level up → earn cosmetic roles/milestones.
- **Concepts**: Anti-spam XP curves, rate limits.
- **Admin controls**: XP rates, role rewards, blacklisted channels.

## Giveaways
- **User flow**: Start giveaway → auto collect entrants → pick winners → post result.
- **Concepts**: Weighted/standard draws, eligibility rules.
- **Admin controls**: Duration, prize, number of winners, anti-alt checks.

## Announcements
- **User flow**: Scheduled/instant announcements to selected channels with embeds.
- **Concepts**: Scheduling, templating, localization.
- **Admin controls**: Target channels, recurrence, time zones.

## Raid × Availability
- **User flow**: Members submit availability → organizer schedules raid → conflicts highlighted.
- **Concepts**: Availability matrices, consensus scheduling, reminders.
- **Admin controls**: Window for responses, thresholds, role filters.

## Rates
- **User flow**: Members query rate tables (e.g., drop rates or server boosts).
- **Concepts**: Versioned tables, effective dates, caching.
- **Admin controls**: CRUD for rates with audit/history.

## Calendar
- **User flow**: View upcoming events/raids; auto reminders before start.
- **Concepts**: iCal-like recurrence, reminder queues, time zone handling.
- **Admin controls**: Create/edit/delete events, per-role visibility.

## Radio 24/7
- **User flow**: Bot streams audio in a voice channel; simple commands to control.
- **Concepts**: Stream resilience, reconnection, basic queueing.
- **Admin controls**: Source configuration, fallback streams, volume limits.
