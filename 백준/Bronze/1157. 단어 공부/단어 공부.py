word = input().lower()

char_count = {}

for char in word:
    if char.isalpha():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

max_count = max(char_count.values())


max_chars = [char for char, count in char_count.items() if count == max_count]


if len(max_chars) > 1:
    print('?')
else:
    print(max_chars[0].upper())