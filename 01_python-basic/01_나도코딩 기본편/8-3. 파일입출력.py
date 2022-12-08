# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100") # write 메소드는 줄바꿈이 없음
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# # 파일의 모든 내용을 다 읽어와서 출력해줌
# print(score_file.read()
# score_file.close()


# score_file = open("score.txt", "r", encoding="utf8")
# # readline() 자체가 줄을 바꿔줌, print()도 줄을 바꿔줌
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# score_file.close()


# # 반복시켜서 readline()사용
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()


score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # readlines()는 list 형태로 저장됨
for line in lines:
    print(line, end="")


