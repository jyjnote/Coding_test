N = int(input())
F = int(input())

front = N // 100
remainder = divmod(front * 100, F)[1]

if remainder != 0:
    answer = F - remainder
else:
    answer = 0

print(f'{answer:02}')