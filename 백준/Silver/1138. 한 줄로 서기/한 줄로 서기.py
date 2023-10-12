N = int(input()) 
t = list(map(int, input().split())) 
r = []
for i in range(N, 0, -1):
    r.insert(t[i-1], i)
for person in r:
    print(person, end=' ')
