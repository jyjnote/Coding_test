import math

a, b = map(int, input().split())

for i in range(a, b + 1):
    if i < 2:
        is_prime = False
    elif i == 2:
        is_prime = True
    elif i % 2 == 0:
        is_prime = False
    else:
        d = math.isqrt(i) + 1
        is_prime = True
        for _ in range(3, d, 2):
            if i % _ == 0:
                is_prime = False
                break
        
    if is_prime:
        print(i)
