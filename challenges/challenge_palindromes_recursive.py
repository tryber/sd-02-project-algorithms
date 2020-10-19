def is_palindrome_recursive(word, low, high):
    if word == "" and low == 0:
        return False

    if low > high:
        return True

    if word[0] == word[-1]:
        low += 1
        high -= 1
        word = word[1:-1]
        return is_palindrome_recursive(word, low, high)
    else:
        return False


word = ""
print(is_palindrome_recursive(word, 0, len(word) - 1))
