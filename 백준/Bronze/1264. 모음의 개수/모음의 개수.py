moum = ['a', 'e', 'i', 'o', 'u']

while True:
    s = input()
    if s == '#':
        break

    count = 0
    for i in moum:
        count += s.lower().count(i)  

    print(count)