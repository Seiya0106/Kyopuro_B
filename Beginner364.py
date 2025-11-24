h, w = map(int, input().split())
si, sj = map(int, input().split())
si -= 1
sj -= 1
C = []
for _ in range(h):
    C.append(list(input()))
X = list(input())

for x in X:
    if x == "L":
        if si >= 0 and si < h and (sj - 1) >= 0 and (sj - 1) < w:
            if C[si][sj - 1] == ".":
                sj -= 1
    elif x == "R":
        if si >= 0 and si < h and (sj + 1) >= 0 and (sj + 1) < w:
            if C[si][sj + 1] == ".":
                sj += 1
    elif x == "U":
        if (si - 1) >= 0 and (si - 1) < h and sj >= 0 and sj < w:
            if C[si - 1][sj] == ".":
                si -= 1
    elif x == "D":
        if (si + 1) >= 0 and (si + 1) < h and sj >= 0 and sj < w:
            if C[si + 1][sj] == ".":
                si += 1
print(si + 1, sj + 1)
