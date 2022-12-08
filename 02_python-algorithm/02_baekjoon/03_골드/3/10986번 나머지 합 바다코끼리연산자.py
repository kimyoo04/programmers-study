import sys; input = sys.stdin.readline
from math import comb

def solution():
    _, m = map(int, input().split())
    nums = [*map(int, input().split())]
    
    counter = [0] * m
    counter[(s := 0)] = 1
    
    for num in nums:
        counter[(s := (s + num) % m)] += 1
        
    print(sum(comb(i, 2) for i in counter))

solution()