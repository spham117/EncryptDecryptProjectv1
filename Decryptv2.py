import math

encoded_input = input("enter code: ")

byte_list = encoded_input.split(sep=",",maxsplit=-1)
byte_list1 = list(map(int,byte_list))
shift = input("enter shift coefficient(integers): ")
coefficient = int(shift)
pend_list = byte_list1
pend_list1 = [(val+coefficient**2)//(coefficient**3) for val in pend_list]
pend_list2 = list(map(chr,pend_list1))
list_join = ''.join(pend_list2)
print(list_join)

