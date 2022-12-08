import sys; input = sys.stdin.readline
# from itertools import accumulate 

# n 리스트의 길이, m 구간의 합
n, m = map(int, input().split())
# 받을 리스트
A = list(map(int, input().split()))

S = [0] * n # 합 배열 저장할 리스트 선언
C = [0] * m # 나머지 숫자들을 카운트할 인덱스 얻기
S[0] = A[0] # 합 배열을 만들기 위해 0 인덱스만 미리 할당
answer = 0 # 정답 찾을 용도로 변수 초기화

# 합 배열 저장
for i in range(1, n):
  S[i] = S[i-1] + A[i]

# 다른 합 배열 저장 방법. S = [*accumulate(A)] 

for i in range(n):
  remainder = S[i] % m
  # 나머지 0인 경우 카운트
  if remainder == 0:
    answer += 1
  # 각 나머지 숫자별 개수
  C[remainder] += 1

for i in range(m):
  if C[i] > 1:
    answer += (C[i] * (C[i] - 1) // 2) # 3C2 4C2 5C2 등 조합의 공식은 이와 같다.

print(answer)