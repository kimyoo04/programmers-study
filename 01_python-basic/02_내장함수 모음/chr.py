# ord(문자) : 문자의 ASCII 코드를 반환한다.
# chr(숫자) : 숫자에 대응하는 문자를 반환한다.


# a 부터 z 까지 출력
for i in range(ord('a'),ord('z')+1):
    print(chr(i), end=" ")

print()

# A 부터 Z 까지 출력
for i in range(ord('A'),ord('Z')+1):
    print(chr(i), end=" ")