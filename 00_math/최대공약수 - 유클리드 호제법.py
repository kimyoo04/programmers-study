a, b = 315, 495
if(b>a) : a,b = b,a

while(b!=0):
    a=a%b
    a,b=b,a

print(a)



a, b = 315, 495

while(a!=b):
    if(a>b) : a-=b
    else    : b-=a

print(a)


# 3개 이상의 수의 최대공약수를 구하려면 반목을 통해 2개씩 비교해 나온 최대공약수와 다음 수를 비교를 계속 한다...


array = [18, 30, 102]

def gcd_function(a, b):
    while(a!=b):
        if(a>b) : a-=b
        else    : b-=a
    return a

for i in range(1, len(array)):
    if i == 1:
        gcd = gcd_function(array[i-1], array[i])
    else:
        gcd = gcd_function(gcd, array[i])

print(gcd)