import sys

ws = []
for i in range(5):  
  w = sys.stdin.readline().rstrip()
  ws.append(w)

for i in range(15): 
  for j in range(5): 
    if i < len(ws[j]):
      print(ws[j][i], end="")