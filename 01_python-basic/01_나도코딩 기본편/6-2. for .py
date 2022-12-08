# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# 위의 내용을 줄여보자!

# for 반복문 

for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(5):  # 0,1,2,3,4 = 순서대로 할 떄!
    print("대기번호 : {0}".format(waiting_no))


# Starbucks에서 

starbucks = ["아이언맨", "토르", "아이엠 그루트"]

for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

# 리스트에 있는 객체들을 한꺼번에 출력 할 수도 있다. 