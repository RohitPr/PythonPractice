# Find Duplicate Words in a string and replace the characters with "(" or ")" depending upon if they occured in the sentence more than Once. Does not depend upon the case of the letter.


def dup_words(word):
    transform_word = word.lower()
    new_word = ""
    for a in transform_word:
        if transform_word.count(a) > 1:
            new_word += ")"
        else:
            new_word += "("
    return new_word


print(dup_words('Hello Hagrid'))
