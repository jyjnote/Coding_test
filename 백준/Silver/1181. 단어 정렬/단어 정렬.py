n = int(input())
words = []

for _ in range(n):
    word = input().strip()
    words.append(word)


unique_words = sorted(set(words), key=lambda x: (len(x), x))

for word in unique_words:
    print(word)
