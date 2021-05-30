#!/bin/python3

# Day 0: Mean, Median, and Mode
# https://www.hackerrank.com/challenges/s10-basic-statistics/problem

from collections import Counter

def mean_median_mode(n, xs):
  xs = sorted(xs)
  
  mean = sum(xs) / n
  
  middle = n // 2
  median = sum(xs[middle-1:middle+1]) / 2 if n % 2 == 0 else xs[middle]

  c = Counter(xs)
  mode = min([k for k, v in c.items() if v == c.most_common(1)[0][1]])
  
  return mean, median, mode

n = int(input().rstrip())
xs = list(map(int, input().rstrip().split(' ')))

mean, median, mode = mean_median_mode(n, xs)

print(f'{mean:.1f}')
print(f'{median:.1f}')
print(f'{mode:.1f}')