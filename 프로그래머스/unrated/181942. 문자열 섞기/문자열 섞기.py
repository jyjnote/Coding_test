def solution (str1, str2):
    result = ''
    for char1, char2 in zip(str1, str2):
        result+=char1
        result+=char2
    return result
