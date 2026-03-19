import argparse
import sys

from no_fucking_try_again.detector import detect_hits
from no_fucking_try_again.messages import BANNER, random_hit_message
from no_fucking_try_again.trigger import send_keystroke


def main():
    parser = argparse.ArgumentParser(
        prog="fafo",
        description="Hit your MacBook to make Claude Code try again.",
    )
    parser.add_argument("--threshold", type=float, default=0.5, help="G-force delta to trigger (default: 0.5)")
    parser.add_argument("--cooldown", type=float, default=1.5, help="Seconds between triggers (default: 1.5)")
    parser.add_argument("--sample-rate", type=int, default=100, help="Accelerometer Hz (default: 100)")
    parser.add_argument("--target", type=str, default="iTerm2", help="Target app name (default: 'iTerm2')")
    parser.add_argument("--dry-run", action="store_true", help="Print instead of sending keystrokes")
    parser.add_argument("--message", type=str, default="no, fucking try again", help="Message to type (default: 'no, fucking try again')")
    parser.add_argument("--no-claude-only", action="store_true", help="Send keystrokes to any tab, not just Claude Code")
    parser.add_argument("--verbose", action="store_true", help="Print live accelerometer readings")
    args = parser.parse_args()

    print(BANNER)
    print(f"  threshold: {args.threshold}g | cooldown: {args.cooldown}s | message: \"{args.message}\"")
    if args.dry_run:
        print("  mode: DRY RUN (no keystrokes will be sent)")
    if args.target:
        print(f"  target: {args.target}")
    print("\n  Listening for hits... (Ctrl+C to quit)\n")

    try:
        for hit in detect_hits(
            threshold=args.threshold,
            cooldown=args.cooldown,
            sample_rate=args.sample_rate,
            verbose=args.verbose,
        ):
            print(f"\n  💥 {random_hit_message()}")
            print(f"     magnitude={hit.magnitude:.2f}g  delta={hit.delta:.2f}g\n")
            send_keystroke(args.message, target=args.target, dry_run=args.dry_run, claude_only=not args.no_claude_only)
    except KeyboardInterrupt:
        print("\n\n  Peace out. ✌️\n")
        sys.exit(0)
