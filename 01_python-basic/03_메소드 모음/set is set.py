a = {1, 2, 3}
b = a

print(a is b) # True
print(a == b) # True

c = a.copy()
print(a is c) # False
print(a == c) # True