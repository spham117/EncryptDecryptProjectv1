
string = input("enter string: ")
shift = input("enter shift coefficient(integers): ")
coefficient = int(shift)
stored_var = ""
def encrypt(string,coefficient,shift,stored_var):
    # """
    # The function encrypts a given string by applying a mathematical formula to each character and
    # returns the encrypted value.
    
    # :param string: The `string` parameter is the input string that you want to encrypt
    # :param coefficient: The coefficient is a numerical value that is used in the encryption algorithm.
    # It is raised to the power of 2 and then multiplied with the ASCII value of each character in the
    # string
    # :param shift: The "shift" parameter represents the number of positions to shift each character in
    # the string
    # :param stored_var: The `stored_var` parameter is a variable that is used to store the encrypted
    # string. It is initially passed as an empty string and is updated with each iteration of the loop in
    # the `encrypt` function
    # :return: The code is returning the encrypted value of the input string.
    # """
    for i in string:
        x = ((ord(i) * abs(coefficient**2))+ coefficient)+ ord(i)
        y = str(x)
        stored_var +=y
    return(int(stored_var))
print(hex(encrypt(string,coefficient,shift,stored_var)))
