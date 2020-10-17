def is_anagram(first_string, second_string):
    if first_string[::-1] == second_string:
        return True
    word_st = list(first_string)
    word_nd = list(second_string)
    for i, letter in enumerate(word_st):
        if letter != word_nd[i]:
            index_letter = word_nd.index(letter)
            word_st[i], word_st[index_letter] = word_st[index_letter], word_st[i]
    if word_st == word_nd:
        return True
    else:
        return False


first_string = "futuro"
second_string = "furtou"
print(is_anagram(first_string, second_string))
