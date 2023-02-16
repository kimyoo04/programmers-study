import sys
w = int(sys.stdin.readline())

arr = [0, 1, 2]
for i in range(3, w+1):
    arr.append(arr[i-1] + arr[i-2])

print(arr[w] % 10007)