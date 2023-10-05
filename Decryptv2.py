import math
import re
import sys


encoded_input = input("enter code: ").rstrip(',')
if not re.match("\d+", encoded_input):
     print ("Error! Only integers allowed!")
shift = input("enter shift coefficient(integers): ")

coefficient1 = ((encoded_input.count(',')+1) * int(shift))

byte_list = encoded_input.split(sep=",",maxsplit=-1)
byte_list1 = list(map(int,byte_list))
byte_list2 = [(item + coefficient1)+(int(shift)**3) for item in byte_list1]

if not re.match("\d+", shift):
     print ("Error! Only integers allowed!")
try:
     pend_list = byte_list2
     pend_list1 = [((val+int(shift)**3)//(int(shift)**3)) for val in pend_list]  
     pend_list2 = list(map(chr,pend_list1))
     list_join = ''.join(pend_list2)
     print(list_join)
except:
    print("An error has occurred. Please try again.")