pri=[]
d={i:int(input()) for i in range(1,9)}


sor=sorted(d.values())[::-1][:5]

for i ,v in d.items():
    if v in sor:
        pri.append(i)
print(sum(sor))
print(*pri)