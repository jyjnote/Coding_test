t = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))

print(len(set(b).difference(a))+len(set(a).difference(b)))