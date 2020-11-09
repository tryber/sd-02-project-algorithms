def is_palindrome_iterative(word):
    if not word:
        return False
    middle = len(word) // 2
    high = len(word) - 1
    for index in range(0, middle):
        if word[index] != word[high - index]:
            return False
    return True


def is_phrase_palindrome(phrase):
    string_phrase = "".join(phrase.split()).lower()
    return is_palindrome_iterative(string_phrase)

word = ""
print(is_palindrome_iterative(word))

word = "COXINHA"
print(is_palindrome_iterative(word))
word = "REVIVER"
print(is_palindrome_iterative(word))
phrase = "MELODRAMA IS THE ALBUM MUBLA EHT SI AMARDOLEM"
print(is_phrase_palindrome(phrase))

