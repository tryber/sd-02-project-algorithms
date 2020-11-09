def is_palindrome_recursive(word, low, high):
    if not word:
        return False
    if low >= high:
        return True
    if word[low] == word[high] and low != high:
        return is_palindrome_recursive(word, low + 1, high - 1)
    return False


def is_phrase_palindrome(phrase):
    string_phrase = "".join(phrase.split()).lower()
    return is_palindrome_recursive(string_phrase, 0, len(string_phrase) -1)
word = ""
print(is_palindrome_recursive(word, 0, len(word) - 1))
word = "COXINHA"
print(is_palindrome_recursive(word, 0, len(word) - 1))
word = "REVIVER"
print(is_palindrome_recursive(word, 0, len(word) - 1))
phrase = "MELODRAMA IS THE ALBUM MUBLA EHT SI AMARDOLEM"
print(is_phrase_palindrome(phrase))