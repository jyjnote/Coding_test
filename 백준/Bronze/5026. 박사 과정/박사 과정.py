t = int(input())  

for _ in range(t):
    a = input().strip()
    if a=='P=NP':
        print('skipped')
    else:
        print(eval(a))