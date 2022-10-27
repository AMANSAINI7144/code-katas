#!/usr/bin/env python3

import sys
sys.path.append("..")

from ansi import *
from comp import *

def get_row(sequence):
    l = 0
    r = 127

    for i in range(7):
        mid = l + (r - l) // 2
        if sequence[i] == "F":
            r = mid - 1
        elif sequence[i] == "B":
            l = mid + 1
        else:
            raise Exception(f"forbidden symbol {sequence[i]}")

    return mid
        

def solve(prob, inputname):
    lines = []
    gen = yield_line(inputname)

    for line in gen:
        lines.append(line)

    print_arr(lines)

    print(f"{len(lines)} in the array")

    if prob == 1:
        return 1
    elif prob == 2:
        return 2
    else:
        print("Invalid problem code")
        exit()
