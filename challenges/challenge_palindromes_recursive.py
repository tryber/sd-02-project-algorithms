def is_palindrome_recursive(word, low, high):
    if high <= low:
        return True
    if word[low] != word[high]:
        return False
    return is_palindrome_recursive(word, low + 1, high - 1)


word = "socacos"
print(is_palindrome_recursive(word, 0, len(word) - 1))
