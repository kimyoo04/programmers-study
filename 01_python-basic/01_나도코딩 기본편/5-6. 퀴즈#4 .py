# Quiz)  당신의 학교에서는 파이썬 코딩 대회를 주최합니다. 
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다. 
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다. 
# 추첨 프로그램을 작성하시오. 

# 조건1 : 편의상 댓글은 20명이 작성하였고, 아이디는 1~20 이라고 가정 
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가 
# 조건3 : random 모듈의 shuffle 과 sample을 활용

# (출력예제) 
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --
'''
(활용예제)
from random import *
st = [1,2,3,4,5]
print(st)
shuffle(st)
print(st)
print(sample(st,1))  # 랜덤으로 숫자를 뽑을 수 있다.sampling

#조건1. 
range(1,21)
#조건2. 
random, 집합형 
#조건3. 
'''
'''체크 필요!!!!!
from random import *

IDlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


치킨당첨자 = randint(1, 20)
del IDlist[치킨당첨자] # 리스트에서 치킨당첨자가 빠짐

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(치킨당첨자))

나머지 = IDlist

커피당첨자 = sample(나머지, 3) 
print("커피 당첨자 : {0}".format(커피당첨자[:]))
print("-- 축하합니다 --")

''' 
from random import *

users = range(1,21)  # 1~20까지 숫자를 생성/ 일일이 다 생성해 줄 필요가 없다. 
print(type(users))
users = list(users)  # [list] 로 변경해야 한다. 
print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 한번에 4명을 추출하게 되면 중복될 일이 없다.

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")

