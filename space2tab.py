#!/usr/bin/env python3

import sys
import re
import os
import argparse


def convert_space(lines):
    new_lines = list()

    for line in lines:
        re_result, number = re.subn('\s+', '\t', line)
        new_lines.append(re_result)
    return new_lines


def main():
    usage = "Usage: " + sys.argv[0] + " input_file output_file"

    # Check arguments
    if len(sys.argv) != 3:
        print("ERROR: Wrong Number of Arguments Provided\n")
        print(usage)
        exit(1)

    # Read Lines
    try:
        with open(sys.argv[1], "r") as inputFile:
            lines = inputFile.read().splitlines()
        lines = "\n".join(convert_space(lines))

    except FileNotFoundError:
        print("Error: \"" + sys.argv[1] + "\" not found.\n")
        print(usage)
        exit(1)

    # Write Lines
    try:
        with open(sys.argv[2], "w") as outputFile:
            outputFile.writelines(lines)

    except FileNotFoundError:
        print("Error: \"" + sys.argv[2] + "\" not found.\n")
        print(usage)
        exit(1)

main()
