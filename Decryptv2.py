unicode = input("enter code: ")
shift = input("enter shift coefficient: ")
shiftint = int(shift)
b = unicode.strip(" ")
for i in b:
    x = chr(i)
    y = str(x)
    z = ' '.join(y)
    a = z.strip(" ")
    print (a, end=" ")
    