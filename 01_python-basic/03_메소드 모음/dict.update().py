# 수정과 추가가 가능함

x = { 'a': 10, 'b': 5}

x.update(a=15)
x.update(a=12, b=23)
print(x) # {'a': 12, 'b': 23}


y = { 1:'one', 2:'two'}
y.update({1:'ONE', 2:'TWO', 3:'THREE'})
print(y) # {1: 'ONE', 2: 'TWO', 3: 'THREE'}


z = { 1:'one', 2:'two'}
z.update([[3, 'three'], [5, 'five']]) # 2차원 배열 가능
z.update(zip([3, 5], ['three', 'five'])) # zip으로 표현 가능
print(z) # {1: 'one', 2: 'two', 3: 'three', 5: 'five'}