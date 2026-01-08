S = input()
cnt = 0
for s in S[1:]:
    if s == "|":
        print(cnt, end=" ")
        cnt = 0
    elif s == "-":
        cnt += 1
print()
