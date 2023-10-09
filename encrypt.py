
while input != "":
    string = input("enter string: ")
    shift = input("enter shift coefficient(integers =< 31): ")
    coefficient = abs(int(shift))

    if coefficient <= 31:
        for i in string:
            x = (((ord(i) * coefficient**3) - coefficient**3) - (((len(string)*coefficient))))- coefficient**3
            y = str(x)
            z = ''.join(y)
            print((z),end=',')


            #This for loop will first encode the user's string input value to UTF-8 integer value then will multiply the integer
            #value with a user defined coefficient integer, which would be a way of scrambling the data(even though this is a very basic method of doing so)
    else:
        print("READ THE INSTRUCTIONS PLEASE >:(")