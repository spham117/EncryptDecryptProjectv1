string = input("enter string: ")
shift = input("enter shift coefficient(integers): ")
coefficient = int(shift)
for i in string:
    x = ((ord(i)**2 * abs(coefficient**2))+ coefficient + 1)+ ord(i)*2
    y = str(x)
    print (hex(y), end="")