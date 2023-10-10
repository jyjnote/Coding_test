
def f(n):
    return 1 if n == 0 else n * f(n - 1)

n, k = map(int,input().split())
print(int(f(n)/(f(k)*f(n-k))))