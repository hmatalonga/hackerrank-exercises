#!/bin/python3

# Day 1: Standard Deviation
# https://www.hackerrank.com/challenges/s10-standard-deviation/problem

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    n = len(arr)
    mean = sum(arr) / n
    s = sum([math.pow(e - mean, 2) for e in arr])
    result = math.sqrt(s / n)
    print(f'{result:.1f}')
    return

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
