n = int(input())
status = {} 
for _ in range(n):
    name, action = input().split()
    status[name] = (action == 'enter')
for name, is_enter in sorted(status.items(), reverse=True):
    if is_enter:
        print(name)
