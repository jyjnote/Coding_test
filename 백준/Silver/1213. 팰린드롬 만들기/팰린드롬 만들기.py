name = input().strip()
name_list = sorted(name)

count = {}
for char in name_list:
    count[char] = count.get(char, 0) + 1

odd_count = 0
odd_alpha = ''
ans = ''

for char, char_count in count.items():
    if char_count % 2 != 0:
        odd_count += 1
        odd_alpha += char

    ans += char * (char_count // 2)

if odd_count > 1:
    print("I'm Sorry Hansoo")
elif odd_count == 0:
    print(ans + ans[::-1])
else:
    print(ans + odd_alpha + ans[::-1])
