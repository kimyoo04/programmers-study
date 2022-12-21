# https://www.acmicpc.net/problem/10816

from sys import stdin
from collections import Counter

n = stdin.readline()
cards = stdin.readline().split()
m = stdin.readline()
array = stdin.readline().split()

counter = Counter(cards)
print(counter)
print(' '.join(f'{counter[m]}' if m in counter else '0' for m in array))