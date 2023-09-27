string = input("enter string: ")
shift = input("enter shift coefficient(integers): ")
coefficient = int(shift)
for i in string:
    x = ord(i) * ((coefficient)**2)
    y = str(x)
    z = ''.join(y)
    print ((hex(int(z))), end=" ")
    print(z)

    