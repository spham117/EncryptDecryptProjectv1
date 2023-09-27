
string = input("enter encoded message: ")
shift = input("enter shift coefficient(integers): ")
coefficient = int(shift)
stored_var = ''

def twos_complement(string, bits):
    value = int(string, 16)
    if value & (1 << (bits - 1)):
        value -= 1 << bits
    return value
a = int(twos_complement(string,16))/int(shift)
b = int(a)
c = str(b)
print(c)
    