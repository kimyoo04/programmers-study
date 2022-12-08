# Dictionary

# key 와 value 형태로 나온다. 
# key에 대한 중복이 허용이 되지 않는다. 

cabinet = {3:"유재석", 100:"김태호"}  # key-3, value-유재석.....

print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3)) # 유재석
# .get을 사용할 때 소괄호를 쓸 수 있다. 

# cabinet에 없는 키 값 5를 넣어줄 때의 차이 
"print(cabinet[5])"  #ERROR
print(cabinet.get(5)) #NONE
# .get을 사용하면 객체값이 없어도 실행이 된다. 

# None 말고 다른 문자가 출력 가능하다.
print(cabinet.get(5, "사용가능"))  # 사용가능

# 키 값이 있는지 없는지 확인할 수 있다. 
print(3 in cabinet)  # True 
print(5 in cabinet)  # False
# (key) in (cabinet)을 통해 판별 가능 

# key 값에는 '정수' 뿐만 아니라 문자열도 가능하다.
cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새로운 키값을 입력할 수 있다. 
print(cabinet)
cabinet["A-3"] = "김종국"  # value값도 바꿀 수 있다. 
cabinet["C-20"] = "조세호" # 새로운 key값을 넣을 수 있다. 
print(cabinet)

# ket값을 없앨 때, 
del cabinet["A-3"]
print(cabinet)
# del (함수?) 쓴다. 

# key값들만 출력할 때
print(cabinet.keys())
# .keys를 쓴다. 

# value 들만 출력할 떄
print(cabinet.values())
# .values를 쓴다. 

# key, value 쌍으로 출력할 때
print(cabinet.items())
# .items를 쓴다. 

# 모든 값을 없앨 때 
cabinet.clear()
print(cabinet) 
# .clear 사용 
