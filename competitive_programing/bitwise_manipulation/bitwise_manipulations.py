#Add
def add(a,b):
  #assign values
  #complexity: o(n), n-> number of bits
  a_temp=a
  b_temp=b
  #sum up using a_temp, carry with b_temp
  while b_temp!=0:  #if no carrry, terminate
    carry=a_temp&b_temp #Check with carry is there or not
    a_temp=a_temp^b_temp #Check and gives the 0 in the summ
    b_temp=carry<<1 #left shift hte carry to next MSB
  return a_temp

#subtract
def sub(a,b):
  #same as add, but we will compliment the answers. Added extra to handle a<b
    #complexity: o(n), n-> number of bits

  a_temp=a
  b_temp=b
  if a<b:
    a_temp,b_temp=b_temp,a_temp
    is_negative=True
  else:
    is_negative=False
  while b_temp!=0:
    borrow=~a_temp&b_temp
    a_temp=a_temp^b_temp
    b_temp=borrow<<1
  if is_negative:
    a_temp=-a_temp
  return a_temp

#parity
def parity(x):
  #complexity o(1)
  x^=x>>32
  x^=x>>16
  x^=x>>8
  x^=x>>4
  x^=x>>2
  x^=x>>1
  return x & 1

