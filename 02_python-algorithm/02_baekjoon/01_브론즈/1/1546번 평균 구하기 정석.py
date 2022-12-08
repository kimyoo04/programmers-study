# https://www.acmicpc.net/problem/1546

'''
식을 단순화하기

(A / M * 100 + B / M * 100 + C / M * 100) / 3 = (A + B + C) * 100 / M / 3
'''

n = int(input())
scores = input().split(" ")

scores = list(map(lambda x: int(x), scores))
max_scores = max(scores)
sum_scores = sum(scores)

print(sum_scores * 100 / max_scores / n)
