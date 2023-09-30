
string = input("enter string: ")
shift = input("enter shift coefficient(integers): ")
coefficient = int(shift)

for i in string:
    x = (ord(i) * coefficient**3) - coefficient**3
    y = str(x)
    a = y.zfill(10)
    z = ''.join(a[::-1])
    print(z ,end=',')
    #remember to omit the trailing comma after retrieving the output
    #This for loop will first encode the user's string input value to UTF-8 integer value then will multiply the integer
    #value with a user defined coefficient integer, which would be a way of scrambling the data(even though this is a very basic method of doing so)
