# isdisjoint : 교집합이 없으면 True, 있으면 False
a = {1, 2, 3}
b = {4, 5, 6}
i = a.isdisjoint(b)
print(i) # True

c = {1, 2, 3}
d = {3, 4, 5}
j = c.isdisjoint(d)
print(j) # False