import time
import sys

lines = [
    "So I’m calling you in the middle of the night",
    "Like it’s the last night on Earth",
    "If the world was ending",
    "You’d come to me, right?",
    "I’d wanna be next to you",
    "And die with a smile",
    "If the world was ending",
    "You’d come to me, right?",
    "I’d wanna be next to you",
    "And die with a smile"
]

delays = [0.6, 0.7, 1.6, 4, 6, 1, 6, 3, 1.7, 2, 0.9, 0.8, 1.0]

for i, line in enumerate(lines):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(delays[i])
    print()