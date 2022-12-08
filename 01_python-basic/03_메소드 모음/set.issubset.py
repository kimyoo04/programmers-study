# issubset : 부분집합 여부 확인
a = {1, 2, 3, 4, 5}
b = {1, 2, 3}
g = a.issubset(b)
print(g) # False
g = b.issubset(a) # b가 a의 부분집합 인지
print(g) # True

