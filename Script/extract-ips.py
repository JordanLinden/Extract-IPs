#!/usr/bin/env python3
#
# Quick script to demonstrate parsing command-line args, reading in files, and matching on regex
# Pass as an argument the path of a text file containing IP addresses, such as a webserver log
# Please note that this script is for learning purposes only and is not suitable for production applications
#
# Jordan Linden @https://github.com/JordanLinden
#

import sys
import pathlib
import re


def extract_ips(contents):
    # Use regex to extract all IP addresses
    pattern = '(?:[0-9]{1,3}\.){3}[0-9]{1,3}'
    ips = re.findall(pattern, contents)
    
    # Output every IP found to the console
    for ip in ips:
        print(str(ip))

def main():
    # Check that a file path was given on the command line
    if len(sys.argv) < 2:
        print("Please provide a file path")
        return 1

    # Store path object
    file_path = pathlib.Path(sys.argv[1])

    # Check that the path is valid
    if not file_path.is_file():
        print("File not found")
        return 1

    # Read file contents
    contents = file_path.read_text()
    
    # Extract IP addresses
    extract_ips(contents)
    
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
