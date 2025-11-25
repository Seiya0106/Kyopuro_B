n = int(input())
D = list(map(int, input().split()))

ans = 0
for i, d in enumerate(D):
    month = str(i + 1)
    for x in range(d):
        day = str(x + 1)
        if len(set(month + day)) == 1:
            ans += 1
print(ans)
