def is_palindrome_recursive(word, low, high):
    if (word[low].lower() != word[high].lower()):
        return False
    else:
        return True
    return is_palindrome_recursive(word, low + 1, high - 1)


word = "Socos"
print(is_palindrome_recursive(word, 0, len(word) - 1))
