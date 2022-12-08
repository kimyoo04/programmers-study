s = {1, 2, 3}
print(f'set : {s}')
 
s.add('blockdmask')
print(f'set : {s}')
 
s.add('blockdmask') # 중복 값 오류 무시
print(f'set : {s}')
 
s.add(4)
print(f'set : {s}')