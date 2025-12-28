#Estimating Polygenic Cancer Risk with the help of probability
# Libraries (do not edit)
from ast import literal_eval
from itertools import product
def polygenic_disease_risk(n, k, mutation_probs):
    # Your code here
  mutation_result=('M','NM') # M = Mutated, NM = Not Mutated
  total_combos=list(product(mutation_result,repeat=n)) #possible combination, Cartesian product rule
  M_counter={}
  for combo in total_combos:
    M_counter[combo]=combo.count('M')
  risky_mutations=[]
  for result,count in M_counter.items():
    if count>=k:
      risky_mutations.append(result)
  total_prob=0
  probability_counter=1
  for risky_mutation in risky_mutations:
    for i in range(len(risky_mutation)):
      if risky_mutation[i]=='M':
        probability_counter*=mutation_probs[i]
      else:
        probability_counter*=(1-mutation_probs[i])
    total_prob+=probability_counter
    probability_counter=1
  return total_prob
# Input and output handling (do not edit)
print(round(polygenic_disease_risk(*literal_eval(input())), 4))
