import random
import string
def add_letters(org,num):
    new_word = ''
    for i in org:
        randomLetter = "".join(random.choice(string.ascii_letters) for _ in range(num))
        new_word += i
        new_word += randomLetter 
    return new_word

original = input('Enter something you can remember: ')
for num in range(5,6):
    #scramble the word using 'num' extra characters
    scrambled = add_letters(original,num)
    #output
    
    print("Adding",num,'random characters to',original,'->',random.shuffle(scrambled))
