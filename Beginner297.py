S = input()
B = []
R = []
k = 0
for i, s in enumerate(S):
    if s == "B":
        B.append(i + 1)
    elif s == "R":
        R.append(i + 1)
    elif s == "K":
        k = i + 1
if ((B[0] % 2 == 0 and B[1] % 2 != 0) or (B[0] % 2 != 0 and B[1] % 2 == 0)) and (R[0] < k and k < R[1]):
    print("Yes")
else:
    print("No")
