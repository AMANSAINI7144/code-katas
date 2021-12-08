#!/usr/bin/env python3

import sys
import math

from math import gcd, floor, sqrt, log
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

MOD = 1000000007

inputname = "jason"
inputname = "real"
inputname = "small"
inputname = "example"

letters = {
    1: "cf",
    7: "acf",
    4: "bcdf",
    2: "acdeg",
    3: "acdfg",
    5: "abdfg",
    0: "abcefg",
    6: "abdefg",
    9: "abcdfg",
    8: "abcdefg",
}

digit = {
    "cf": 1,
    "acf": 7,
    "bcdf": 4,
    "acdeg": 2,
    "acdfg": 3,
    "abdfg": 5,
    "abcefg": 0,
    "abdefg": 6,
    "abcdfg": 9,
    "abcdefg": 8,
}

def deduce(letters):
    if len(letters) == 2:
        return 1
    if len(letters) == 3:
        return 7
    if len(letters) == 4:
        return 4
    if len(letters) == 5:
        if "f" in letters:
            if "c" in letters:
                return 3
            return 5
        return 2
    if len(letters) == 6:
        if "c" in letters:
            if "e" in letters:
                return 0
            return 9
        return 6
    if len(letters) == 7:
        return 8

translate = {}

lines = open(inputname, "r").read().splitlines()

count = 0

for line in lines:
    left, right = line.split(" | ")
    signals = [word for word in left.split()]
    signals = ["".join(sorted(word)) for word in left.split()]
    result = [word for word in right.split()]
    result = ["".join(sorted(word)) for word in right.split()]
    for signal in signals:
        if len(signal) == 2:
            translate[signal[0]] = "c"
            translate[signal[1]] = "f"
        elif len(signal) == 3:
            translate[signal[0]] = "a"
            translate[signal[1]] = "c"
            translate[signal[2]] = "f"
        elif len(signal) == 4:
            translate[signal[0]] = "b"
            translate[signal[1]] = "c"
            translate[signal[2]] = "d"
            translate[signal[3]] = "f"
    print(signals)
    print(result)
    tmp = []
    for word in result:
        broken = list(word)
        for i in range(len(broken)):
            broken[i] = translate.get(broken[i], "?")
        result = "".join(broken)
        res = deduce(result)
        tmp.append(str(res))
    tok = int("".join(tmp))
    print(tok, "\n")
    count += tok

print(count)
