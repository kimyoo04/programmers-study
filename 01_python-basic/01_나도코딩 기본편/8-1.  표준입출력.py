print("Python", "Java")
print("Python" + "Java")


print("=" * 50)
print("Python", "Java", sep=" vs ") # vs 가 문자열과 문자열 사이에 들어간다.


print("=" * 50)
print("Python", "Java", end="?") # 
print("무엇이 더 재미있을까요?")


print("=" * 50)
import sys
print("Python", "Java", file=sys.stdout) # 실제는 표준출력으로 문장이 찍힘 
print("Python", "Java", file=sys.stderr) # 실제는 표준에러로 문장이 찍힌다.


print("=" * 50)
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    # ljust(숫자)는 왼쪽으로 숫자만큼 정렬
    # rjust(숫자)는 오른쪽으로 숫자만큼 정렬
    # score은 정수형이기 때문에 str로 변환후 적용.
    print(subject.ljust(8), str(score).rjust(4), sep=":")


print("=" * 50)
for num in range(1, 21):
    # .zfill(숫자)는 0을 숫자만큼 자리를 확보하고 나타낸다.
    print("대기번호 : " + str(num).zfill(3))


print("=" * 50)
answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")