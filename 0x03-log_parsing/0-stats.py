#!/usr/bin/python3
import sys
import re


def print_statistics(total_size, status_codes):
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


def parse_line(line, total_size, status_codes):
    f = (
        r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] '
        r'"GET /projects/260 HTTP/1.1" (\d+) (\d+)'
        )
    m = re.match(f, line)
    if m:
        file_size = int(m.group(4))
        status_code = m.group(3)
        total_size += file_size
        status_codes[status_code] = status_codes.get(status_code, 0) + 1
        return total_size, status_codes
    else:
        return total_size, status_codes


def main():
    total_size = 0
    status_codes = {}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            total_size, status_codes = parse_line(line.strip(),
                                                  total_size, status_codes)
            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)
    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        sys.exit(0)


if __name__ == "__main__":
    main()
