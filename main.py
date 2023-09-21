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
def add_numbers(org,num):
    new_num = ''
    for i in org:
        randomNumber = "".join(random.choice(string.ascii_letters) for _ in range(num+1))
        new_num += i
        new_num += randomNumber
    return new_num
original = input('Enter something you can remember: ')
for num in range(1,2):
    #scramble the word using 'num' extra characters
    scrambled = add_letters(original,num)+ add_numbers(original,num) 
    #output
    
    print("Adding",num,'random characters to',original,'->',scrambled)