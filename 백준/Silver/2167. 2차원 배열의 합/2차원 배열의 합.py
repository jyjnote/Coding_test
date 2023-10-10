
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

P = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        P[i][j] = A[i - 1][j - 1] + P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1]

for _ in range(K):
    i, j, x, y = map(int, input().split())
    result = P[x][y] - P[x][j - 1] - P[i - 1][y] + P[i - 1][j - 1]
    print(result)
