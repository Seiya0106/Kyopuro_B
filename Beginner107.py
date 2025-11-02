H, W = map(int, input().split())
a = []
r1 = []
r2 = []
for _ in range(H):
    a.append(list(input()))

# 横
row_has_black = [any(cell == "#" for cell in row) for row in a]
# 縦
col_has_black = [any(a[i][j] == "#" for i in range(H)) for j in range(W)]

for i in range(H):
    if row_has_black[i]:
        print(''.join(a[i][j] for j in range(W) if col_has_black[j]))
