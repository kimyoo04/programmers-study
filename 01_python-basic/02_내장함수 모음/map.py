# 입력
# 5
# 1 1
# 2 3
# 3 4
# 9 8
# 5 2

# 출력
# 2
# 5
# 7
# 17
# 7

# map 함수 안쓸 때
num = int(input("반복횟수")) # 5

for x in range(num):
    a,b = input("A B").split()
    print(int(a) + int(b))

# map 함수
t = int(input())  # 테스트 케이스 개수 t를 입력받음    

for _ in range(t):  # t 만큼 반복
    a,b = map(int,input().split())
    print(a+b)