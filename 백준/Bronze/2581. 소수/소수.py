def ip(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

m = int(input())
n = int(input())

prime_sum = 0
min_prime = float('inf')

for i in range(m, n + 1):
    if ip(i):
        prime_sum += i
        min_prime = min(min_prime, i)

print(-1 if prime_sum == 0 else f"{prime_sum}\n{min_prime}")
