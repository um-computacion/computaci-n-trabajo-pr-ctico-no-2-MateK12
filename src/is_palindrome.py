def is_palindrome(word):
    if len(word) <= 1:
        return False
    word = word.replace(':','').replace(',','').replace('.','').replace('?','').replace("'",'').replace(" ",'').lower()
    reverse_word = word[::-1]
    if reverse_word == word:
        return True 
    else: return False
