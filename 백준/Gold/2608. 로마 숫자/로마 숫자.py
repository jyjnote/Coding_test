def r(n):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    t = 0
    p = 0

    for c in reversed(n):
        v = d[c]
        if v < p:
            t -= v
        else:
            t += v
        p = v

    return t

def a(n):
    d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    r = ''

    for v, l in d.items():
        c = n // v
        r += l * c
        n -= v * c

    return r

r1 = input().strip()
r2 = input().strip()
a_sum = r(r1) + r(r2)
print(a_sum)
print(a(a_sum))
