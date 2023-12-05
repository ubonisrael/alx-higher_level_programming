#!/usr/bin/python3
"""A script that collects data about requests
and prints them at intervals.
"""
import sys

file_size = 0
status_codes = {'200': 0, '301': 0, '400': 0,
                '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
count = 0


def print_stats(stat_codes_obj, f_size):
    """Prints the stats about the status codes. """
    print("File size: {:d}".format(f_size))
    for k, v in stat_codes_obj.items():
        if v > 0:
            print("{:s}: {:d}".format(k, v))


try:
    for line in sys.stdin:
        count += 1
        line_list = line.split()

        try:
            file_size += int(line_list[-1])
        except (IndexError, ValueError):
            pass

        try:
            code = line_list[-2]
            if code in status_codes:
                status_codes[code] += 1
        except IndexError:
            pass

        if count % 10 == 0:
            print_stats(status_codes, file_size)
except KeyboardInterrupt as e:
    print_stats(status_codes, file_size)
    raise
