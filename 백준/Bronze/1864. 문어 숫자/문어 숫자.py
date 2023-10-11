char_to_number = {
    '/': -1,
    '-': 0,
    '\\': 1,
    '(': 2,
    '@': 3,
    '?': 4,
    '>': 5,
    '&': 6,
    '%': 7,
}


while 1:
    s=input()
    count=-1
    total=0
    if s=='#':
        break
    for i in s[::-1]:
        if i in char_to_number.keys():
            count+=1
            total+=char_to_number.get(i)*8**(count)
    print(total)
  