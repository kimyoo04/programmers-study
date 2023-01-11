# https://school.programmers.co.kr/learn/courses/30/lessons/49191

'''
문제
- 선수 수 n은 100 이하
- 경기결과 result는 4500 이하
- [A, B] = A가 B를 이겼다.

-> 정확하게 순위를 매길 수 있는 선수의 수 구하기
'''

'''
필요지식
- 플로이드 워셜 활용 : 한 다리 건너를 파악하는 알고리즘, 3중 for 문
- 유향그래프
- 인접행렬, 2차원 배열의 활용력 필요

핵심
- 승리, 패배, 모르는 것을 구분 (True, False, None)
- None이 존재하면 정확하게 순위를 매길 수 있는 선수
'''


def solution1(n, results):
    matrix = [[None for _ in range(n)] for _ in range(n)]

    # 0 인덱스부터 활용
    for win, lose in results:
        matrix[win-1][lose-1] = True
        matrix[lose-1][win-1] = False

    # a -> k -> b
    for k in range(n):
        for a in range(n):
            for b in range(n):
                if matrix[a][k] == None:
                    continue

                if matrix[a][k] == True and matrix[k][b] == True:
                    matrix[a][b] = True
                elif matrix[a][k] == False and matrix[k][b] == False:
                    matrix[a][b] = False


    answer = 0

    # matrix[i][i] 제외 None 유무 파악
    for i in range(n):
        if None not in matrix[i][:i] + matrix[i][i+1:]:
            answer += 1
    return answer


# 다른 풀이

"""
- "?", "WIN", "LOSE", "SELF"로 총 4가지로 구분
- "?"가 없으면 정확하게 순위를 매길 수 있는 선수
"""

def solution2(n, results):
    # 인접행렬 생성
    total = [['?' for i in range(n)] for j in range(n)]

    # SELF로 먼저 처리
    for i in range(n):
        total[i][i] = 'SELF'

    # 주어진 results로 값 넣기
    for result in results:
        total[result[0]-1][result[1]-1] = 'WIN'
        total[result[1]-1][result[0]-1] = 'LOSE'

    # i -> k -> j
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if total[i][k] == 'WIN' and total[k][j] == 'WIN':
                    total[i][j] = 'WIN'
                elif total[i][k] == 'LOSE' and total[k][j] == 'LOSE':
                    total[i][j] = 'LOSE'

    answer = 0

    for i in total:
        if '?' not in i:
            answer += 1

    return answer


a = solution1(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
print(a)