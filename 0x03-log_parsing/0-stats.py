#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Print the accumulated metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def handle_signal(sig, frame):
    """Handle keyboard interruption (CTRL + C) and print stats."""
    print_stats()
    sys.exit(0)

# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, handle_signal)

try:
    for line in sys.stdin:
        parts = line.split()

        # Check if the line matches the required format
        if len(parts) < 7:
            continue

        try:
            ip = parts[0]
            date = parts[3] + " " + parts[4]
            request = parts[5] + " " + parts[6] + " " + parts[7]
            status_code = int(parts[8])
            file_size = int(parts[9])
        except (ValueError, IndexError):
            continue  # Skip malformed lines

        # Update metrics
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1

        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle keyboard interruption gracefully
    print_stats()
    sys.exit(0)
