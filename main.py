string = input("enter string: ")
shift = input("enter shift coefficient(integers): ")
coefficient = int(shift)
stored_var = ""
for i in string:
    x = ((ord(i)**2 * abs(coefficient**2))+ coefficient + 1)+ ord(i)*2
    y = str(x)
    stored_var +=y
    z = int(stored_var)
    t = hex(z)
    print (y, end=" ")
    print(z)
    print (t)