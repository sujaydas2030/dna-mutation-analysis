#Encrypting DNA-Like Sequences with Lightweight Mapping(Encrypting DNA Codes)
from itertools import product #importing to create the pairs
def encrypt_bases(input_bases):
    # Your code here
  standard_bases='ACGT'
  standard_bases_pairs=list(''.join(pair_base) for pair_base in product(standard_bases,repeat=2))
  no_standartd_bases= 'HIMOPQ'
  encrypted_bases=""
  #running through manual while loop, as we need to access the i+1 item
  i=0
  while i < len(input_bases):
    #checking if the i+1 is inside the loop and the pairs are in the standard_bases_pairs
    if i+1<len(input_bases) and input_bases[i]+input_bases[i+1] in standard_bases_pairs:
      encrypted_bases+=chr(97+standard_bases_pairs.index(input_bases[i]+input_bases[i+1]))
      i+=2
    #if it is not a pair and inside no_standard_bases
    elif input_bases[i] in no_standartd_bases:
      encrypted_bases+=chr(97+20+no_standartd_bases.index(input_bases[i]))
      i+=1
    #if it is not a pair and inside the standard_bases
    else:
      encrypted_bases+=chr(97+16+standard_bases.index(input_bases[i]))
      i+=1
  return encrypted_bases
# Input and output processing (do not edit)
print(encrypt_bases(input()))
