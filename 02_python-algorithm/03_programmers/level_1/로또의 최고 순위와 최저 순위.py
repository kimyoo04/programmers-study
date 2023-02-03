# https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    rank = 7
    zeros = 0
    ranks = []

    for lot_num in lottos:
        if lot_num in win_nums :
            rank -= 1
        elif lot_num == 0 :
            zeros += 1

    ranks = [rank - zeros, rank]

    if zeros == 6:
        return [1, 6]
    elif ranks[0] == 7:
        return [6, 6]

    return ranks