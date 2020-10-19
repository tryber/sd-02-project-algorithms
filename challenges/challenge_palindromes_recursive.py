def is_palindrome_recursive(word, low, high):
    if (high == -1):
        return False
    result = True
    if (word[low].lower() != word[high].lower()):
        return not result
    elif (low >= high):
        return result
    else:
        result = is_palindrome_recursive(word, low + 1, high - 1)
        return result


word = ""
print(is_palindrome_recursive(word, 0, len(word) - 1))
