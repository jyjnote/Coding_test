N = int(input())
fn = [input() for _ in range(N)]

p = ""
for i in range(len(fn[0])):
    c = fn[0][i]
    for j in range(1, len(fn)):
        if fn[j][i] != c:
            p += "?"
            break
    else:
        p += c

print(p)
