#to get LSB:
def get_lsb(x):
    #whatever the value is the it will be ANDed with 001 >> returns only if LSB is 1, otherwise 0
    return x & 1

#to get the value of the LSB bit set to 1
def get_lsb_val(x):
    #returns the value of the first bit set to 1
    return x&~(x-1)

#clear the bit set to 1 at the first LSB
def clear_lsb(x):
    return x&(x-1)

#to check if any particulary bit set to 1
def bit_1(x,bit):
    return x & 1<<bit

#swap bits in a number
