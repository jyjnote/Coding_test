a,b = map(int, input().split())
d = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', 
     '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}

li = []
for _ in range(a, b+1):
    s = ' '.join([d[c] for c in str(_)])
    li.append([_, s])
li.sort(key=lambda x:x[1])
for _ in range(len(li)):
    if _%10 == 0 and _!= 0:
        print()
    print(li[_][0], end=' ')