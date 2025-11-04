N = int(input())
S = input()
ans = []
for s in S:
    uni = ord(s)
    uni += N
    if uni > 90:
        uni -= 26
    ans.append(chr(uni))
for a in ans:
    print(a, end="")
print()
