n, k = map(int, input().split())
S = input()
words = dict()
for i in range(n - k + 1):
    if S[i:i+k] in words:
        words[S[i:i+k]] += 1
    else:
        words[S[i:i+k]] = 1

top = max(words.values())
print(top)
dic = []
for k, v in words.items():
    if v == top:
        dic.append(k)
dic.sort()
print(*dic)
