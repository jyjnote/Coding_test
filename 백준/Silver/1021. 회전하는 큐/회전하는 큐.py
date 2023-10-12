from collections import deque

N, M = map(int, input().split())
positions = list(map(int, input().split()))
q = deque(range(1, N + 1))
moves = 0

for target_position in positions:
    left_moves = 0
    while q[0] != target_position:
        q.rotate(1)
        left_moves += 1

    right_moves = len(q) - left_moves
    moves += min(left_moves, right_moves)
    q.popleft()

print(moves)
