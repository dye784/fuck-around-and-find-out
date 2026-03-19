import subprocess


def send_keystroke(message: str, target: str | None = None, dry_run: bool = False):
    """Type a message + Enter into the frontmost terminal (or a specific app) via osascript."""
    if dry_run:
        print(f"  [dry-run] would type: {message}")
        return

    if target:
        script = f'''
tell application "{target}" to activate
delay 0.3
tell application "System Events"
    keystroke "{message}"
    keystroke return
end tell
'''
    else:
        script = f'''
tell application "System Events"
    keystroke "{message}"
    keystroke return
end tell
'''

    subprocess.run(["osascript", "-e", script], capture_output=True, timeout=5)
