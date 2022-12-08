def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t 나이 : {1}\t".format(name, age), end = " ") # end= "" 는 다음문장까지 같이 print하겠다. 
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "","","")

# 더 추가할 사항이 생길 상황을 대처 

def profile(name, age, *language):
    print("이름 : {0}\t 나이 : {1}\t".format(name, age), end = " ")
    for lang in language:       # language는 계속 반복되게끔 한다. 
        print(lang, end="")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")