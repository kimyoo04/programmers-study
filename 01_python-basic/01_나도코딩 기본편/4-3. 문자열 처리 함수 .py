python = "Python is Amazing"

# 소문자로 변경할 때
print(python.lower())

# 대문자로 변경할 때 
print(python.upper())

# 문장의 첫번째가 대문자인지 판별할 때 
print(python[0].isupper())

# 문자열의 길이 
print(len(python))

# 다른 문자로 바꾸고 싶을 때
print(python.replace("Python", "Java"))

# n이 들어간 첫번째 index
index = python.index("n")
print(index)

# 시작점을 설정해준다. 첫번째 n을 찾은 그 지점부터  (두번째 n을 찾는)
index = python.index("n", index + 1 ) 
print(index)

# 비슷한 함수로는 find
print(python.find("n"))
# 하지만 index와 차이점이 있다. 
# input 값에 속하지 않는 단어를 넣었을 경우 
# find는 -1 로  처리하고 계속 진행하지만, 
# index는 에러가 뜨면서 멈춰버린다. 
print(python.find("Java"))
print(python.index("Java"))


# 몇 번 사용한지 알아볼 때
print(python.count("n"))

