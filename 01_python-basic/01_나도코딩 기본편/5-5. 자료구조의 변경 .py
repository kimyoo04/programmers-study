
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu)
print(menu, type(menu))
# {단순 집합형} 

menu = list(menu)
print(menu, type(menu))
# [리스트형]

menu = tuple(menu)
print(menu, type(menu))
# (튜플형) 

menu = set(menu)
print(menu, type(menu))
# 다시 set을 씌우면 
# {단순 집합형} 으로 설정된다. 
