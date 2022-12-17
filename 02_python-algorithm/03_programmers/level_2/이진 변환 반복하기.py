# >>> bin(0b101010) 2진수
# '0b101010'
# >>> oct(0b101010) 8진수
# '0o52'
# >>> hex(0b101010) 16진수
# '0x2a'
# >>> str(0b101010) 10진수
# '42'


def solution(s):
    answer = []
    zeros = 0
    loop = 0
    nums = list(map(int, s))
    
    while len(nums) != 1:
        zero_count = nums.count(0)
        zeros += zero_count
        loop += 1
        
        # 0 없는 1의 개수 재할당 
        nums = len(nums) - zero_count
        
        # 2진수 변환
        nums = list(map(int, bin(nums)[2:]))
        print(nums)
        
    answer.append(loop)
    answer.append(zeros)
    return answer
  

def solution1(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]
