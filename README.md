# no-fucking-try-again

Hit your MacBook to make Claude Code try again.

```
  ___         _       _                       _
 | __|  _ ___| |__   /_\  _ _ ___ _  _ _ _  __| |
 | _| || / __| / /  / _ \| '_/ _ \ || | ' \/ _` |
 |_| \_,_\___|_\_\ /_/ \_\_| \___/\_,_|_||_\__,_|
  _           _   ___ _         _    ___       _
 /_\  _ _  __| | | __(_)_ _  __| |  / _ \ _  _| |_
/ _ \| ' \/ _` | | _|| | ' \/ _` | | (_) | || |  _|
\_/ \_\_||_\___| |_| |_|_||_\__,_|  \___/ \_,_|\__|
```

Uses the Apple Silicon accelerometer to detect when you physically hit your MacBook, then types "no, fucking try again" into Claude Code (or any terminal app).

## Requirements

- Apple Silicon MacBook (M-series) with accelerometer
- `sudo` for hardware access
- Accessibility permissions for your terminal app

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Usage

Run in a **separate terminal** from Claude Code:

```bash
# Default: sends keystrokes to iTerm2
sudo .venv/bin/fafo

# Dry run — detect hits without sending keystrokes
sudo .venv/bin/fafo --dry-run --verbose

# Target a different app
sudo .venv/bin/fafo --target "Terminal"

# Custom message
sudo .venv/bin/fafo --message "try harder"

# Lower sensitivity (trigger on smaller hits)
sudo .venv/bin/fafo --threshold 0.3
```

## CLI Flags

| Flag | Default | Description |
|------|---------|-------------|
| `--threshold` | `0.5` | G-force delta to trigger |
| `--cooldown` | `1.5` | Seconds between triggers |
| `--sample-rate` | `100` | Accelerometer Hz |
| `--target` | `iTerm2` | Target app for keystrokes |
| `--dry-run` | `False` | Print instead of sending keystrokes |
| `--message` | `"no, fucking try again"` | Message to type |
| `--verbose` | `False` | Print live accelerometer readings |

## How It Works

1. Streams accelerometer data from the Apple Silicon IMU via [`macimu`](https://github.com/olvvier/apple-silicon-accelerometer)
2. Maintains a rolling baseline (~1g at rest)
3. When the delta between current magnitude and baseline exceeds the threshold — you hit it
4. Sends the message as keystrokes to the target app via `osascript`

## Percussive Debugging

When frustration meets engineering.

## Credits

Inspired by [spank](https://github.com/taigrr/spank).

Sensor reading and vibration detection ported from [apple-silicon-accelerometer](https://github.com/olvvier/apple-silicon-accelerometer).

## License

[MIT](LICENSE)
