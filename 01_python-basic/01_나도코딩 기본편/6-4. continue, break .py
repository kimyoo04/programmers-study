
absent = [2, 5] #결석 

for student in range(1, 11): # 1~10까지 학생이 있다
    if student in absent:
        continue
    print("{0}, 책을 읽어봐".format(student))

# Continue는 스킵하고 계속 진행! (끝까지 반복!)

no_book = [7]  # 책을 깜박함.

for student in range(1, 11): # 1~10까지 학생이 있다
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지, {0} 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

# break는 걸리면 바로 중단한다. (for탈출한다.)