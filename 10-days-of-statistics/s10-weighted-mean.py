#!/bin/python3

# Day 0: Weighted Mean
# https://www.hackerrank.com/challenges/s10-weighted-mean/problem

import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
  n = len(X)
  return sum([X[i] * W[i] for i in range(n)]) / sum(W)


if __name__ == '__main__':
  n = int(input().strip())

  vals = list(map(int, input().rstrip().split()))

  weights = list(map(int, input().rstrip().split()))

  mean = weightedMean(vals, weights)

  print(f'{mean:.1f}')