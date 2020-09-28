# Trolls are attacking your comment section!A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat. Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!". Note: for this kata y isn't considered a vowel.

def disemvowel(string):
    for i in "aeiouAEIOU":
        string = string.replace(i, "")
    print(string)
    return string
            
            
    
disemvowel('chris')
disemvowel('This website is for losers LOL!')

# another way
def disemvowel(string):
    return string.translate(None, "aeiouAEIOU")

# another way
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")

# using a while loop
def disemvowel(str2handle):
    vowel_character = ["a", "A", "e", "E", "o", "O", "i", "I", "u", "U"]
    str2return = ""
    i = 0
    n = len(str2handle)
    while i < n:
        if not str2handle[i] in vowel_character:
            str2return += str2handle[i]
        i += 1
    return str2return