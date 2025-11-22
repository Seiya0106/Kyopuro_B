N = int(input())
A = list(map(int, input().split()))
flag = True
for i in range(N - 2):
    if A[i + 2] * A[i] != A[i + 1] * A[i + 1]:
        flag = False
if flag:
    print("Yes")
else:
    print("No")
