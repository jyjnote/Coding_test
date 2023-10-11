A, B =input().split()
mi = int(A.replace('6', '5')) + int(B.replace('6', '5')) 
ma = int(A.replace('5', '6')) + int(B.replace('5', '6'))
print(mi, ma)