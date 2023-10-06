def solution(strings, n):
    
    char_with_strings = [(s[n], s) for s in strings]
   
    char_with_strings.sort()

    
    return [string for char, string in char_with_strings]