N, Q = map(int, input().split())
T = list(map(int, input().split()))
teeth = [True for _ in range(N)]
for t in T:
    if teeth[t - 1] == True:
        teeth[t - 1] = False
    else:
        teeth[t - 1] = True
print(sum(teeth))
