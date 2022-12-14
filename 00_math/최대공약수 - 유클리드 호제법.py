a, b = 315, 495

# 한 번씩 빼는 방식은 시간복잡도가 높다.
def gcd1(a, b):
    while(a!=b):
        if(a>b) : a-=b
        else    : b-=a
    return a

def gcd2(a, b):
    if b == 0:
        return a
    else:
        return gcd2(b, a%b)

result = gcd2(a, b)
print(result)

# 3개 이상의 최대공약수 구하기
# 반목을 통해 2개씩 비교해 나온 최대공약수와 다음 수를 비교를 계속 한다...
array = [18, 30, 102]

for i in range(1, len(array)):
    if i == 1:
        result = gcd2(array[i-1], array[i])
    else:
        result = gcd2(result, array[i])

print(result)