n, m = map(int, input().split())
S = []
T = []
for _ in range(n):
    s = list(input())
    S.append(s)
for _ in range(m):
    t = list(input())
    T.append(t)

for i in range(n - m + 1):
    for j in range(n - m + 1):
        ok = True
        for k in range(m):
            for v in range(m):
                if S[k + i][v + j] != T[k][v]:
                    ok = False
        if ok:
            print(i + 1, j + 1)
