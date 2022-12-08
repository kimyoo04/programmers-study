a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

# issuperset : issubset과 반대 superset인지 확인
h = a.issuperset(b)
print(h) # True
h = b.issuperset(a) # b가 a의 부분집합의 반대인지
print(h) # False
