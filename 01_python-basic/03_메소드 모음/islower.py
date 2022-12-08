# string.islower() 예제1 
s1 = 'Python'
s2 = s1.lower() 
print('{0} 대문자? : {1}'.format(s1, s1.islower())) # False 
print('{0} 대문자? : {1}'.format(s2, s2.islower())) # True 

# ==========================================================

# string.islower() 예제2 
s3 = 'a B 2 $%' 
for i in s3: 
    print('\'{0}\'는 대문자? : {1}'.format(i, i.islower()))