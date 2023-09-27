unicode = input("enter code: ")
shift = input("enter shift coefficient: ")
shift_int = int(shift)
b = unicode.strip(" ")
for i in b:
    x = chr(i)
    z = ' '.join(x)
    a = z.strip(" ")
    print (a, end=" ")
    