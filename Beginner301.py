n = int(input())
A = list(map(int, input().split()))

for i in range(n-1):
    dif = abs(A[i]-A[i+1])
    if dif == 1:
        print(A[i], end=" ")
    elif A[i]<A[i+1]:
        for j in range(A[i], A[i+1]):
            print(j, end=" ")
    else:
        for k in range(A[i], A[i+1], -1):
            print(k, end=" ")
print(A[n-1])
