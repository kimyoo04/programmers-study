
# 지하철 칸별로 10명, 20명, 30명 
subway1 = 10 
subway2 = 20
subway3 = 30 

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]

# 조세호씨가 몇번째 칸에 타고 있는가? 
print(subway.index("조세호"))
# .index는 그 객체가 위치를 알 수 있다. (0부터 시작)

#하하씨가 다음 정류장에서 다음 칸에 탑승 
subway.append("하하") 
print(subway)
# .append는 뒤부분에만 붙일 수 있다.  

# 정형돈씨를 유재석 / 조세호 사이에 태워봄.
subway.insert(1, "정형돈")
print(subway)
# 중간에 값을 넣기 위해서는 .insert(index, 객체)를 사용한다. 

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄.
print(subway.pop())
print(subway)
# .pop은 마지막에 있는 객체 뺄 때 사용한다.(삭제할때)

# 같은 이름의 사람이 몇 명 있는지 확인.
subway.append("유재석") 
print(subway.count("유재석"))
# .count는 객체 수를 측정할 수 있다. 

# 정렬도 가능하다. 
num_list = [1, 3, 2, 7, 4, 6, 5]
num_list.sort()
print(num_list)
# .sort는 리스트를 순서대로(오름차순) 재정렬해준다. 

# 순서 뒤집기도 가능하다.
num_list = [1, 3, 2, 7, 4, 6, 5]
num_list.reverse()
print(num_list)
# .reverse는 리스트의 순서를 뒤집는다. 

# 모두 지우기 
num_list.clear()
print(num_list)
# .clear는 리스트 안의 객체 삭제 

# 다양한 자료형 함께 사용 
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장도 가능하다. 
num_list = [1, 3, 2, 7, 4, 6, 5]
num_list.extend(mix_list)
print(num_list)
# .extend는 ()의 리스트와 합칠 수 있다. 

