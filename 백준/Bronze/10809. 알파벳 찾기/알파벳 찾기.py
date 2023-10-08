word = input() 
alphabet_positions = [-1] * 26 

for i in range(len(word)):
    idx = ord(word[i]) - ord('a') 
    if alphabet_positions[idx] == -1:
        alphabet_positions[idx] = i 

for position in alphabet_positions:
    print(position, end=' ')