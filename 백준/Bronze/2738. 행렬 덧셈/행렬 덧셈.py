a,b = map(int, input().split())  

A = []
for _ in range(a):
    row = list(map(int, input().split()))
    A.append(row)

B = []
for _ in range(a):
    row = list(map(int, input().split()))
    B.append(row)

result = [[A[i][j] + B[i][j] for j in range(b)] for i in range(a)]

for row in result:
    print(*row)
