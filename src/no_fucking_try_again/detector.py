import math
import time
from collections import deque
from dataclasses import dataclass


@dataclass
class HitEvent:
    timestamp: float
    magnitude: float
    delta: float


def detect_hits(threshold: float = 0.5, cooldown: float = 1.5, sample_rate: int = 100, verbose: bool = False):
    """Stream accelerometer data and yield HitEvents when a slap is detected."""
    from macimu import IMU

    imu = IMU(sample_rate=sample_rate, gyro=False)
    imu.start()
    baseline_window = deque(maxlen=sample_rate)  # ~1 second of samples
    last_hit_time = 0.0

    try:
        for x, y, z in imu.stream_accel():
            mag = math.sqrt(x * x + y * y + z * z)
            now = time.time()

            # Update baseline from non-spike samples
            if baseline_window:
                baseline = sum(baseline_window) / len(baseline_window)
            else:
                baseline = 1.0  # ~1g at rest

            delta = abs(mag - baseline)

            if verbose:
                print(f"  accel  x={x:+.2f}  y={y:+.2f}  z={z:+.2f}  |g|={mag:.2f}  delta={delta:.2f}  thresh={threshold:.1f}")

            if delta > threshold and (now - last_hit_time) > cooldown:
                last_hit_time = now
                if verbose:
                    print()  # newline after the \r line
                yield HitEvent(timestamp=now, magnitude=mag, delta=delta)
            else:
                # Only add non-spike samples to baseline
                baseline_window.append(mag)
    finally:
        imu.stop()
