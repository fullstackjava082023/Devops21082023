def reverse_string(text):
    # return reverse string
    return text[::-1]

def count_occurrences(text, char):
    # "Hello world" , "l"
    # return number of chars in the text
    return text.count(char)

def is_palindrome(text):
    # to check if the word is palindrom we can check if reverse word is the same like original
    result = (text == reverse_string(text))
    return result
