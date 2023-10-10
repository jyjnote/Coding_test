t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    f, r = n % h or h, (n - 1) // h + 1
    print(f * 100 + r)
