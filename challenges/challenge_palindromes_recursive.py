def is_palindrome_recursive(word, low, high):
    if not len(word):
        return False
    if len(word) == 1:
        return True
    if len(word) == 2:
        return word[0] == word[1]
    if word[0] == word[-1]:
        return is_palindrome_recursive(word[1:-1], 0, len(word[1:-1]))
    else:
        return False


word = "asdads"
print(is_palindrome_recursive(word, 0, len(word) - 1))
