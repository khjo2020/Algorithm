N = int(input())

A = [0] * N

for i in range(N):
    A[i] = int(input())

for i in range(N-1):
    for j in range(N-1-i):
        if A[j] > A[j+1]:
            A[j],A[j+1] = A[j+1], A[j]
for i in range(N):
    print(A[i])