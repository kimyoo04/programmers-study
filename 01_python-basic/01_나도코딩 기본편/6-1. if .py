
weather = input("오늘 날씨는 어때요?")
# 질문에 대한 답을 적으면 weather = 답 

# 그 후 그 답에 따라 print되는 문장이 다름.
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

temp = int(input("기온은 어때요?"))
# input으로 들어온 값은 "문자열"이다. 그러므로 숫자형으로 int()를 써서 바꿔줘야 한다. 

if 30 <= temp:
    print("너무 더워요. 나가지 마세요.")
elif 10 <= temp and temp < 30 : 
    print("괜찮은 날씨에요") 
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요.")

# if문은 if - elif(여러번가능, 생략가능) - else 순으로 쓴다. 