#Write a program to accept a character from the user and check whether it is a vowel or consonant using switch statement.

def switch(c):
    switcher = {
        'a':'vowel',
        'A':'vowel',
        'e':'vowel',
        'E':'vowel',
        'i':'vowel',
        'I':'vowel',
        'o':'vowel',
        'O':'vowel',
        'u':'vowel',
        'U':'vowel'
    }
    return switcher.get(c,'consonant')

c=input('Enter a character ')
print(switch(c))