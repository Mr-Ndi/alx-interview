#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code><file size>
(if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption
(CTRL + C), print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous
<file size> (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405, and 500
if a status code doesn’t appear or is not an integer,
don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""

import sys
import re


def initialize_log():
    """Initialize the log dictionary."""
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    log = {
        "file_size": 0, "code_list": {str(code): 0 for code in status_codes}}
    return log


def parse_line(line, regex, log):
    """Parse a line of log and update the log dictionary."""
    match = regex.match(line)
    if match:
        stat_code, file_size = match.group(1), match.group(2)
        log['file_size'] += int(file_size)
        if stat_code in log['code_list']:
            log['code_list'][stat_code] += 1
    return log


def print_codes(log):
    """Print the accumulated file size and status codes."""
    print('File size: {}'.format(log['file_size']))
    for code in sorted(log['code_list'].keys()):
        if log['code_list'][code] > 0:
            print('{}: {}'.format(code, log['code_list'][code]))


def main():
    """Main function to read stdin and process log lines."""
    regex = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] '
        r'"GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
    )
    log = initialize_log()
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            log = parse_line(line, regex, log)
            line_count += 1
            if line_count % 10 == 0:
                print_codes(log)
    except KeyboardInterrupt:
        print_codes(log)
        raise
    print_codes(log)


if __name__ == "__main__":
    main()
