'''
Quiz) 사이트 별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

예) http://naver.com 
규칙1 : http:// 부분은 제외 => naver.com 
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => never
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성 
           (nav)                   (5)           (1)               (!)
예) 생성된 비밀번호 : nav51!
'''
''''
내 답>

Site = "http://naver.com"

print(Site[7:10] + str(len(Site[-9,-4])) + str(Site.count("e")) + "!")
'''
# (answer) 
 
url = "http://naver.com"
my_str = url.replace("http://","") # 규칙1
# print(my_str)
my_str = my_str[:my_str.index(".")] # 규칙2 
# my_str[0:5] -> 0~5직전까지 (0,1,2,3,4,5)
# print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print(password)


# MY Fault = 너무 급했다. 한번에 다 하려고 하지 말고! 나눠서 진행해보자! 
