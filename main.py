import random
import string
from random import shuffle

def add_letters(org,num):
    new_word = ''
    for i in org:
        randomLetter = "".join(random.choice(string.ascii_letters) for _ in range(num+1))
        new_word += i
        new_word += randomLetter 
    return new_word
def add_char(org,num):
    new_char = ''
    for i in org:
        randomChar = "".join(random.choice(string.digits) for _ in range(num+1))
        new_char += i
        new_char += randomChar
    return new_char
def add_char2(org,num):
    new_char2 = ''
    for i in org:
        randomChar2 = "".join(random.choice(string.punctuation) for _ in range(num+1))
        new_char2 += i
        new_char2 += randomChar2
    return new_char2

original = input('Enter something you can remember: ')
for num in range(1,2):
    #scramble the word using 'num' extra characters
    scrambled = add_letters(original,num) + add_char(original,num) + add_char2(original,num)
    #output
    scrambled_list = list (scrambled)
    random.shuffle(scrambled_list)
    result = ''.join(scrambled_list)
    print("Adding",num,'random characters to',original,'->',result)