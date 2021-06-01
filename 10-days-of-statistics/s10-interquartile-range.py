#!/bin/python3

# Day 1: Interquartile Range
# https://www.hackerrank.com/challenges/s10-interquartile-range/problem

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def median(xs):
    n = len(xs)
    middle = n // 2
    return sum(xs[middle-1:middle+1]) / 2 if n % 2 == 0 else xs[middle]


def quartiles(arr):
    n = len(arr)
    middle = n // 2
    arr = sorted(arr)

    q2 = median(arr)
    q1, q3 = (median(arr[:middle]), median(arr[middle:])) if n % 2 == 0 else \
            (median(arr[:middle]), median(arr[middle+1:]))

    return (q1, q2, q3)


def create_array(arr, freq):
    n = len(arr)
    xs = []
    for i in range(n):
        xs += [arr[i]] * freq[i]
    return sorted(xs)

def interQuartile(values, freqs):
    arr = create_array(values, freqs)
    q1, _, q3 = quartiles(arr)
    print(f'{q3-q1:.1f}')
    return

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
