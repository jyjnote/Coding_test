n = int(input())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

an=[]
if sum(a)<sum(b):
    for i in range(len(a)):
        an.append(sorted(a)[i]*sorted(b)[::-1][i])
else:
    for i in range(len(a)):
        an.append(sorted(a)[::-1][i]*sorted(b)[i])
print(sum(an))