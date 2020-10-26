def is_palindrome_recursive(word, low, high):
    if word == "":
        return False
    if len(word) <= 1:
        return True
    if word[low] == word[high]:
        new_word = word[1:-1]
        return is_palindrome_recursive(new_word, 0, len(new_word) - 1)
    else:
        return False


word = "ANA"
print(is_palindrome_recursive(word, 0, len(word) - 1))
