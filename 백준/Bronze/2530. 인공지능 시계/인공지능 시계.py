h, m, s = map(int, input().split())
cooking_time = int(input())

total_seconds = h * 3600 + m * 60 + s + cooking_time
total_seconds %= 86400

print(total_seconds // 3600, (total_seconds % 3600) // 60, total_seconds % 60)
