# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    arr = s.split(" ")
        
    for i in range(len(arr)):
        if arr[i] == '':
            continue
        if not arr[i][0].isdecimal():
            arr[i] = arr[i][0].upper() + arr[i][1:].lower()
        else:
            arr[i] = arr[i][0] + arr[i][1:].lower()
          
    answer =" ".join(arr)
    return answer

a = solution("3BpeBople unFollowed mBBeB")
print(a)

# 문자열 첫글자 대문자로 바꾸기
# string.title() 
# string.capitalize()

def solution1(s):
    answer = ''
    arr=s.split(' ')

    for i in range(len(arr)):
        arr[i]=arr[i].capitalize()
    answer=' '.join(arr)
    return answer