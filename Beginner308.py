N, M = map(int, input().split())
C = list(map(str, input().split()))
D = list(map(str, input().split()))
P = list(map(int, input().split()))
total = 0
for c in C:
    if c in D:
        idx = D.index(c)
        total += P[idx + 1]
    else:
        total += P[0]
print(total)
