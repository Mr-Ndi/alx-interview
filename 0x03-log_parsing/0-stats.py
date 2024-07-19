#!/usr/bin/python3
"""
    importing available modules in order to 
    achive the seted tasks
"""
import sys
from collections import defaultdict


def print_stats(total_size: int, status_codes: dict) -> None:
    """Prints the total file size and the count of each status code.
    Args:
        total_size (int): The total size of files processed.
        status_codes (dict): A dictionary with status codes as keys and
        their counts as values.
    """
    print(f"File size: {total_size}")
    for status_code in sorted(status_codes):
        if status_codes[status_code]:
            print(f"{status_code}: {status_codes[status_code]}")


def main() -> None:
    """Main function to read log lines from stdin, compute metrics,
    and print statistics.
    Reads lines from standard input, processes them to extract file sizes
    and status codes,
    and prints the statistics every 10 lines or upon a keyboard interruption.
    """
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.strip().split()
            if len(parts) != 10 or parts[5][1:4] != "GET":
                continue

            file_size = int(parts[-1])
            total_size += file_size

            status_code = int(parts[6])
            status_codes[status_code] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
