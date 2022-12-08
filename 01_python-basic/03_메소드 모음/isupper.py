# string.isupper() 예제1 
s1 = 'BlockDMask'
s2 = s1.upper() 
print('{0} 대문자? : {1}'.format(s1, s1.isupper())) # False 
print('{0} 대문자? : {1}'.format(s2, s2.isupper())) # True 

# ==========================================================

# string.isupper() 예제2 
s3 = '하이. P y T h O n !' 
for i in s3: 
    print('\'{0}\'는 대문자? : {1}'.format(i, i.isupper()))