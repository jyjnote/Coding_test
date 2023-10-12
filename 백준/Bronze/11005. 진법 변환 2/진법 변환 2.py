def d(num, base):
    if num == 0:
        return '0'

    symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    converted = ''
    
    while num:
        num, rem = divmod(num, base)
        converted = symbols[rem] +converted
    
    return converted


dn, b = map(int, input().split())

result = d(dn, b)

print(result)