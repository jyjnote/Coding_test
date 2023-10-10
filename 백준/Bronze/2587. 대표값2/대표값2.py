import statistics
a=[]
for i in range(5):
    a.append(int(input()))
    
print(statistics.mean(a))
print(statistics.median(a))