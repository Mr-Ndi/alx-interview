#!/usr/bin/python3


import sys
from collections import defaultdict

# Initialize variables
total_file_size = 0
status_codes = defaultdict(int)


# Function to print the statistics
def print_stats():
    """Print the current statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


# Read stdin line by line
line_count = 0
try:
    for line in sys.stdin:
        line_count += 1
        try:
            # Parse the input line
            parts = line.strip().split(" ")
            if len(parts) != 9:
                continue
            ip_address = parts[0]
            date = parts[3][1:-1]
            method = parts[5]
            path = parts[6]
            protocol = parts[7]
            status_code = int(parts[8])
            file_size = int(parts[9])

            # Update the metrics
            total_file_size += file_size
            status_codes[status_code] += 1

            # Print the statistics every 10 lines or on keyboard interrupt
            if line_count % 10 == 0:
                print_stats()
        except (ValueError, IndexError):
            # Skip the line if it doesn't match the expected format
            continue
except KeyboardInterrupt:
    # Print the final statistics on keyboard interrupt
    print_stats()
