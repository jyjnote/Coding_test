n= int(input())
ns =[int(input()) for _ in range(n) ]

ns.sort(reverse=True)


for nb in ns:
    print(nb, end=' ')