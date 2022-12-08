# 내용 변경이나 추가를 할 수 없다. 
# 변경되지 않는 목록을 사용할 때 사용

menu = ("돈까스", "치즈까스")

print(menu[0])  # [index의 번호]를 넣는다. 
print(menu[1])

# .add 기능X
'''
name = "김종국"
age = 20 
hobby = "코딩"
print(name, age, hobby)
'''
##
name, age, hobby = "김종국", 20, "코딩"
print(name) # 김종국 
print(name, age, hobby) # 김종국, 20, 코딩 

# 괄호가 생략된 형태인 것이다. 이때 자료의 순서에 따라 값이 매칭된다. 
(name, age, hobby) = ("김종국", 20, "코딩") 
print(name, age, hobby)