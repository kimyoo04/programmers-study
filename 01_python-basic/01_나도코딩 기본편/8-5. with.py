import pickle

# with 문을 탈출하면 자동으로 close 시킨다.
# with open("profile.pickle", "rb", ) as profile_file: # 리드바이너리
#     print(pickle.load(profile_file))


# with open("study.txt", "w", encoding="utf8") as study_file: # 리드바이너리
#     study_file.write("파이썬을 열심히 공부하고 있어요")


with open("study.txt", "r", encoding="utf8") as study_file: # 리드바이너리
    print(study_file.read())