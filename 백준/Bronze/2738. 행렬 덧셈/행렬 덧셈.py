
N, M = map(int, input().split())


matrix_A = [list(map(int, input().split())) for _ in range(N)]


matrix_B = [list(map(int, input().split())) for _ in range(N)]


result_matrix = [[matrix_A[i][j] + matrix_B[i][j] for j in range(M)] for i in range(N)]

# 결과 행렬 출력
for row in result_matrix:
    print(*row)
