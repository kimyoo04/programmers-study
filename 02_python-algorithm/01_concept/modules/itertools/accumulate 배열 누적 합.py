from itertools import accumulate

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(1, len(a)):
    a[i] += a[i-1]
print(a)  # [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

b = list(accumulate(a))
print(b)  # [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

# for 문 보다 accumulate가 속도 빠름!