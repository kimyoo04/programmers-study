# -*- coding: utf-8 -*-
import sys; input=sys.stdin.readline

val = int(input())

def solution(val):
    sixteen_val = val
    eight_val = val
    answer = []

    while True:
        remain = sixteen_val % 16
        if remain >= 10:
            answer.append(str("ABCDEF"[remain - 10]))
        else:
            answer.append(str(remain))

        moc = sixteen_val // 16
        if moc >= 16:
            sixteen_val = moc
        else:
            if moc >= 10:
                answer.append(str("ABCDEF"[moc - 10]))
                break
            else:
                answer.append(str(moc))
                break

    answer.append(' ')

    while True:
        remain = eight_val % 8
        answer.append(str(remain))

        moc = eight_val // 8
        if moc >= 8:
            eight_val = moc
        else:
            answer.append(str(moc))
            break

    for _ in range(len(answer)):
        print(answer.pop(), end="")

solution(val)