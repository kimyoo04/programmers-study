two_list = []

# [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]......[19, 20]]
i = 1
while i < 20:
    two_list.append([i, i+1])
    i += 2

# two_list를 순차적으로 접근하는 이중 for 구문
for one_list in two_list:
    for item in one_list:
        print(item)