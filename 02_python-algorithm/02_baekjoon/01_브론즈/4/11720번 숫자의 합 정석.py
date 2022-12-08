# https://www.acmicpc.net/problem/11720

# n값 받기
n = input()
# numbers 변수에 list 함수를 이용하여 숫자를 한 자리씩 나누어 받기
numbers = list(input())
sum = 0

# for numbers 검색
for i in numbers:
    # sum 변수에 numbers 에 있는 각 자릿수를 가져와 더하기
    sum += int(i)

# sum 출력
print(sum)