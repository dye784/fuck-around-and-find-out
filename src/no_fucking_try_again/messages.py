import random

BANNER = r"""
  ___         _       _                       _
 | __|  _ ___| |__   /_\  _ _ ___ _  _ _ _  __| |
 | _| || / __| / /  / _ \| '_/ _ \ || | ' \/ _` |
 |_| \_,_\___|_\_\ /_/ \_\_| \___/\_,_|_||_\__,_|
  _           _   ___ _         _    ___       _
 /_\  _ _  __| | | __(_)_ _  __| |  / _ \ _  _| |_
/ _ \| ' \/ _` | | _|| | ' \/ _` | | (_) | || |  _|
\_/ \_\_||_\___| |_| |_|_||_\__,_|  \___/ \_,_|\__|

  no-fucking-try-again v0.1.0
  Hit your MacBook. Claude tries again.
"""

HIT_MESSAGES = [
    "HIT DETECTED. Telling Claude to try the fuck again.",
    "WHACK! Sending 'try again' like you mean it.",
    "POW! Claude better get it right this time.",
    "SMACK! Re-engaging Claude with extreme prejudice.",
    "THWACK! Violence is never the answer. Except now.",
    "BAM! Your MacBook felt that. So will Claude.",
    "BONK! Percussive debugging engaged.",
    "WHAM! That's the spirit. Retrying.",
    "CRACK! Frustration → keystrokes → progress.",
    "KAPOW! Try again, you beautiful disaster.",
]


def random_hit_message() -> str:
    return random.choice(HIT_MESSAGES)
