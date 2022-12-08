# https://www.acmicpc.net/problem/1546

'''
세준이 기말고사 조작 결심
세준이 자기 점수 중 최댓값 고름

최댓값M 
모든 점수를 점수 / M * 100으로 고침
'''


n = int(input())
scores = input().split(" ")
scores = list(map(lambda x: int(x), scores))
max_score = max(scores)

fake_scores = list(map(lambda x: x / max_score * 100, scores))
print(sum(fake_scores) / len(fake_scores))