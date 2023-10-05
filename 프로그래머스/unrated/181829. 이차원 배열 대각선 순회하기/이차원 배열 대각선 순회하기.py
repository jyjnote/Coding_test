def solution(board, k):
    row = len(board)
    col = len(board[0])
    total_sum = 0

    for i in range(row):
        for j in range(col):
            if i + j <= k:
                total_sum += board[i][j]

    return total_sum