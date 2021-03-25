#!/usr/bin/env python3

from pprint import pprint


def get_cpu_info():
    the_info = None
    while the_info is None or 'flags' not in the_info:
        import cpuinfo
        the_info = cpuinfo.get_cpu_info()

    return the_info


def main():
    pprint(get_cpu_info())


if __name__ == "__main__":
    main()

