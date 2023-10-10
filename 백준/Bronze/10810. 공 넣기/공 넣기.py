
N, M = map(int, input().split())


baskets = [0] * N


for _ in range(M):

    start, end, ball_number = map(int, input().split())

    for i in range(start - 1, end):
        baskets[i] = ball_number

for ball in baskets:
    print(ball, end=' ')
