# 가장 큰 양의 정수 a 값 구하기
# 다음 두 조건 중 하나를 만족

# 1. 철수카드의 모든 수자를 나눌 수 있고, 영희카드 하나도 나눌 수 없는 수a
# 2. 1의 반대

from functools import reduce
from math import gcd


def get_gcd(arr):
    def gcd(a, b):
        while(a!=b):
            if(a>b) : a-=b
            else    : b-=a
        return a
    
    g = arr[0]
    for i in range(1,len(arr)):
        g = gcd(g,arr[i])
    return g
    
    


def solution(arrayA, arrayB):
    res = 0
    A, B = get_gcd(arrayA), get_gcd(arrayB)
	# 첫 번째 조건
    for i in arrayB:
        if i % A == 0:
            break
    else:
        res = max(A,res)
	# 두 번째 조건
    for i in arrayA:
        if i % B == 0:
            break
    else:
        res = max(B,res)

    return res


v = solution([10,17], [5, 20])
print(v)




def solution_not_good(arrayA, arrayB):
    def get_gcd(a, b):
        while(a!=b):
            if(a>b) : a-=b
            else    : b-=a
        return a

    for i in range(1, len(arrayA)):
        if i == 1:
            gcdA = get_gcd(arrayA[i-1], arrayA[i])
        else:
            gcdA = get_gcd(gcdA, arrayA[i])
            
            
    for i in range(1, len(arrayB)):
        if i == 1:
            gcdB = get_gcd(arrayB[i-1], arrayB[i])
        else:
            gcdB = get_gcd(gcdB, arrayB[i])

    if gcdA > gcdB:
        return gcdA
    elif gcdB == 1:
        return 0
    else:
        return gcdB
    


def solution2(nums1, nums2):
    gcd1, gcd2 = nums1[0], nums2[0]
    for each1, each2 in zip(nums1[1:], nums2[1:]):
        gcd1, gcd2 = gcd(each1, gcd1), gcd(each2, gcd2)
    answer = []
    for each1 in nums1:
        if each1 % gcd2 == 0:
            break
    else:
        answer.append(gcd2)
    for each2 in nums2:
        if each2 % gcd1 == 0:
            break
    else:
        answer.append(gcd1)
    return max(answer) if answer else 0



def solution3(nums1, nums2):
    gcd1, gcd2 = reduce(gcd, nums1), reduce(gcd, nums2)
    answer = []
    if all(each % gcd2 for each in nums1):
        answer.append(gcd2)
    if all(each % gcd1 for each in nums2):
        answer.append(gcd1)
    return max(answer) if answer else 0


