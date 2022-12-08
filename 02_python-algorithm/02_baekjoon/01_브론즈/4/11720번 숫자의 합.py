# https://www.acmicpc.net/problem/11720

n = int(input(""))
num_length = 0

while num_length != n:
    num_input = input()
    num_input = list(num_input)
    num_length = len(num_input)  
    num_input = list(map(lambda x : int(x), num_input))

print(sum(num_input))