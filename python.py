import math

n = int(input())
a = list(map(int, input().split()))

count = 0

# 1 ~ len(a) - 1
for i in range(1, len(a)):
    for j in range(0, len(a)):
        if a[j] == i:
            count = count + math.floor((j + 1) / 2)
            del a[j]
            break

print(count)