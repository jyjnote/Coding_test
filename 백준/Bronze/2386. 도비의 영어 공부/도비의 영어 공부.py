while True:
    line = input()
    if line == '#':
        break
    
    letter, sentence = line.split(' ', 1)
    letter = letter.lower()
    sentence = sentence.lower()
    
    count = sentence.count(letter)
    print(f"{letter} {count}")
