def solution(s, n):
    result = ""
    for char in s:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + n) % 26 + ascii_offset)
            result += encrypted_char
        else:
            result += char
    return result