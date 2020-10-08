def is_palindrome_recursive(word, low, high):
    if not word:
        return False

    if high <= low:
        return True

    if word[high] != word[low]:
        return False
    else:
        return is_palindrome_recursive(word, low + 1, high - 1)


word = "sopapos"
print(is_palindrome_recursive(word, 0, len(word) - 1))
