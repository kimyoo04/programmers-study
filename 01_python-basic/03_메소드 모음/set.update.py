k = {1, 2, 3}
k.update([3, 4, 5])

print(f'set : {k}') # {1, 2, 3, 4, 5}

s = {1, 2, 3}
print(f'set : {s}')
 
s.update({'a', 'b', 'c'})
print(f'set : {s}')
 
s.update([11, 12, 13])
print(f'set : {s}')