#!/usr/bin/env python3

import sys
import locale
import re

# assign command line arguments, strip
my_word = sys.argv[1]

# set line number and compile regex pattern
line_number = 0
pattern = re.compile(r'\b({0})\b'.format(my_word), flags=re.IGNORECASE)

# open file and search for pattern
with open(sys.argv[2], encoding=locale.getpreferredencoding()) as my_file:
    for current_line in my_file:
        line_number += 1
        if pattern.search(current_line):
            print('{0}    {1}'.format(line_number, current_line.rstrip()))

