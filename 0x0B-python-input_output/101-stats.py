#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics.
"""


import sys

status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
        }
total_size = 0


def print_stats():
    """
    Function to print the stats.
    """
    print("File size: {:d}".format(total_size))
    for status, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {:d}".format(status, count))


try:
    for i, line in enumerate(sys.stdin, 1):
        split_line = line.split()
        if len(split_line) < 2:
            continue
        if split_line[-2] in status_codes:
            status_codes[split_line[-2]] += 1
        total_size += int(split_line[-1])
        if i % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
print_stats()
