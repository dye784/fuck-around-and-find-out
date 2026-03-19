import subprocess


def _get_frontmost_tab_title(target: str) -> str | None:
    """Get the title of the frontmost tab/window of the target terminal app."""
    if target == "iTerm2":
        script = '''
tell application "iTerm2"
    tell current session of current tab of current window
        return name
    end tell
end tell
'''
    elif target == "Terminal":
        script = '''
tell application "Terminal"
    return name of selected tab of front window
end tell
'''
    else:
        return None

    try:
        result = subprocess.run(
            ["osascript", "-e", script], capture_output=True, text=True, timeout=5,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except (subprocess.TimeoutExpired, Exception):
        pass
    return None


def _is_claude_code_active(target: str) -> bool:
    """Check if the frontmost tab in the target app is running Claude Code."""
    title = _get_frontmost_tab_title(target)
    if title is None:
        return True  # can't determine, allow it
    return "claude" in title.lower()


def send_keystroke(
    message: str,
    target: str | None = None,
    dry_run: bool = False,
    claude_only: bool = True,
):
    """Type a message + Enter into the frontmost terminal (or a specific app) via osascript."""
    if dry_run:
        print(f"  [dry-run] would type: {message}")
        return

    if claude_only and target and not _is_claude_code_active(target):
        print("  ⏭️  Skipped — frontmost tab is not Claude Code")
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
