#Filtering Harmful DNA Mutation Patterns
# Libraries (do not edit)
from ast import literal_eval
from itertools import product
def filter_dna_mutations(bases, length, harmful_patterns):
    # Your code here
  permuted_sequence=list(product(bases,repeat=length))
  joined_sequence=[''.join(sequnce_tuple) for sequnce_tuple in permuted_sequence]
  harmless_patterns=[]
  for sequence in joined_sequence:
    if sequence not in harmful_patterns:
      harmless_patterns.append(sequnce)

  return sorted(harmless_patterns)
# Input and output processing (do not edit)
print(filter_dna_mutations(*literal_eval(input())))
