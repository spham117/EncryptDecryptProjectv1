string = input("enter string: ")
shift = input("enter shift coefficient(integers): ")
coefficient = int(shift)


for i in string:
    x = ord(i) * coefficient**3 - coefficient**2
    y = str(x)
    z = ''.join(y)
    #print ((hex(int(z))), end=" ")
    print(z, end=',')
    #This for loop will first encode the user's string input value to UTF-8 integer value then will multiply the integer
    #value with a user defined coefficient integer, which would be a way of scrambling the data(even though this is a very basic method of doing so)
    