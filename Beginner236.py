from collections import Counter

N = int(input())
A = list(map(int, input().split()))
num = Counter(A)
for k, v in num.items():
    if v != 4:
        print(k)
        exit()
