fruit = {'apple':3, 'banana':8, 'grape':7, 'orange':3, 'peach':10}


for k, v in fruit.items():
    print(k.ljust(15,'-') + str(v).rjust(5))

print('hello'.rjust(20, '-'))
print('hello'.ljust(20, '-'))
print('hello'.center(20, '-'))
