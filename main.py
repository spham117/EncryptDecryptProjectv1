string = input("enter string: ")
shift = input("enter shift coefficient(integers): ")
coefficient = int(shift)
stored_var = ""
def encrypt(string,coefficient,shift,stored_var):
    for i in string:
        x = ((ord(i) * abs(coefficient**2))+ coefficient)+ ord(i)
        y = str(x)
        stored_var +=y
    return(int(stored_var))
print(hex(encrypt(string,coefficient,shift,stored_var)))
print(encrypt(string,coefficient,shift,stored_var))
