li = []
n = int(input())
t = list(map(int, input().split()))
s = sorted(t)

for i in range(n):
    id = s.index(t[i])
    li.append(id)
    s[id] = -1
    
    
    
print(*li)