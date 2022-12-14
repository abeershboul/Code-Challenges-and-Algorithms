# Write here the code challenge solution
def repeated_Word(s):
    """
    function that will take a string as a parameter and return the first repeated word in that string
    """


    splited=s.split(' ')
    words=set()
    
    
    for word in splited:
        if word in words:
            return word
        else:
            words.add(word)
    return 'No Repetition'

print(repeated_Word('wellcome to hashtable'))
print(repeated_Word('hashtable wellcome to hashtable'))  