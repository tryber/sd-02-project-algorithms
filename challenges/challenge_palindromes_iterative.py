def is_palindrome_iterative(word):
    low = 0
    high = len(word) - 1
    while high > low:
        if word[low] != word[high]:
            return False
        low += 1
        high -= 1
    return True


word = "socacos"
print(is_palindrome_iterative(word))
