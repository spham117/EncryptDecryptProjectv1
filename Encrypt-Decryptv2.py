string = input("enter string: ")
shift = input("enter shift coefficient(integers): ")
coeff = int(shift)
for i in string:
    x = ord(i) * (((coeff)*(coeff))+3)
    y = str(x)
    z = ' '.join(y)
    print (z, end=" ")

    