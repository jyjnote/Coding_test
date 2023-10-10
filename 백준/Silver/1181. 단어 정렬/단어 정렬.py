n = int(input())  

ws = []  

for i in range(n):
    word = input()
    ws.append(word) 
uw = sorted(set(ws), key=lambda x: (len(x), x))

print(*uw) 
