def sol(n, m, board):
    min_repaint = float('inf')

    for i in range(n - 7):
        for j in range(m - 7):
            repaint = 0
            for x in range(8):
                for y in range(8):
                    if (i + x + j + y) % 2 == 0:
                        if board[i + x][j + y] == 'B':
                            repaint += 1
                    else:
                        if board[i + x][j + y] == 'W':
                            repaint += 1
            min_repaint = min(min_repaint, repaint, 64 - repaint)

    return min_repaint

n, m = map(int, input().split())
board = [input() for _ in range(n)]

print(sol(n, m, board))
