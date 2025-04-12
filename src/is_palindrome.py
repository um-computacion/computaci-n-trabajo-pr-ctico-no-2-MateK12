def is_palindrome(word):

    word = word.replace(':','').replace(',','').replace('.','').replace('?','').replace("'",'').replace(" ",'').lower()
    reverse_word = word[::-1]


word = input('palindromo??')
print(is_palindrome(word))