# # Write here the code challenge solution
from collections import Counter
def repeated_Word(s):
    """
    function that will take a string as a parameter and return the first repeated word in that string
    """


    splited=s.split(' ')
    dict = Counter(splited)
    
    
    for word in splited:
        if word in dict:
            return word
        else:
            dict.add(word)
    return 'No Repetition'

print(repeated_Word('wellcome to hashtable'))
print(repeated_Word('hashtable wellcome to hashtable')) 