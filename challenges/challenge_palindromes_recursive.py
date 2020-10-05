def is_palindrome_recursive(word, low, high):
    if word == '':
        return False
    if low >= high:
        return True
    if word[low] == word[high] and low < high:
        low += 1
        high -= 1
        return is_palindrome_recursive(word, low, high)
    else:
        return False


word = "reviver"
print(is_palindrome_recursive(word, 0, len(word) - 1))
