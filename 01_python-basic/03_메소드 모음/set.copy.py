s = {1, 2, 3}

t = s.copy() # 얕은 복사에 해당
print(s) # {1, 2, 3}
print(t) # {1, 2, 3}

id(s)
id(t) # s와 아이디가 다름

