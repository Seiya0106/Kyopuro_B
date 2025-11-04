L, R = map(int, input().split())
S = input()
s = list(S)
sr = list(S[L - 1:R])
sr.reverse()
for i, k in enumerate(range(L-1, R)):
    s[k] = sr[i]
for j in s:
    print(j, end="")
print()
