'''
gun = 10 

def checkpoint(soldiers): #경계근무
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)  # 2명이 경계 근무 나감 
print("남은 총 : {0}".format(gun))
'''
# 오류가 난다. checkpoint 안에 있는 gun은 정의가 안됐다. (지역변수) 

'''
gun = 10 

def checkpoint(soldiers): #경계근무
    gun = 20
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)  # 2명이 경계 근무 나감 
print("남은 총 : {0}".format(gun))
'''

# 전체 총 : 10, 함수내 남은 총 : 18, 남은 총:10
# 지역변수 안에서만 바꼈다. 밖으로 나온게 없다. 

# 전역 변수를 사용하자 

gun = 10 

def checkpoint(soldiers): #경계근무
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)  # 2명이 경계 근무 나감 
print("남은 총 : {0}".format(gun))


# 전체 총:10, 함수내 남은 총 : 8 , 남은총 :8 
# 전역변수는 권장되지 않는다. 

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}". format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 퐁 : {0}".format(gun))

# 전역 변수 쓰지 않고 전달값 반환값으로 쓰는 것이 좋다. 