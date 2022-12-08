'''
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

customer = "아이언맨"
index = 1
while True:
    print("{0}, 커피가 준비 되었습니다. 호출 {1}회.".format(customer, index))
    index += 1
'''
# 무한 루프 

# Q. 호출 {1}회 부분에 0이 아니라 1를 써준 이유가? 호출 0회는 없으니까 1부터 시작해서 그런가?

customer = "토르"
person = "Unknown"

while person != customer:
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")

# 2:14:57
