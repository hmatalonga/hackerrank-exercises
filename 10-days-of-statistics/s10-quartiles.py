#!/bin/python3

# Day 1: Quartiles
# https://www.hackerrank.com/challenges/s10-quartiles/problem

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
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

  return list(map(int, [q1, q2, q3]))

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  n = int(input().strip())

  data = list(map(int, input().rstrip().split()))

  res = quartiles(data)

  fptr.write('\n'.join(map(str, res)))
  fptr.write('\n')

  fptr.close()
