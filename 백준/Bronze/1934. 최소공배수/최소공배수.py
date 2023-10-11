import math
def c(a, b):
    return (a * b) // math.gcd(a, b)
T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    lcm = c(A, B)
    print(lcm)
