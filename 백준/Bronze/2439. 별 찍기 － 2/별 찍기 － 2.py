height = int(input())

for i in range(1, height + 1):
    spaces = " " * (height - i)
    stars = "*" * i
    print(spaces + stars)
