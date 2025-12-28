#Categorising Mutations Based on Severity Scores, risk identification through quantile
# Libraries (do not edit)
from ast import literal_eval

def count_mutation_risk_groups(scores, label):
    # Your code here
  def quartile(data_set,n): #creating quartile function
    data_set.sort()
    spaces=len(data_set)-1
    k=n
    q=4 # as we are dividing the data set into 4 parts
    index=k*spaces/q
    lower=int(index)
    upper=lower+1
    fraction=index-lower
    value=data_set[lower]+(fraction*(data_set[upper]-data_set[lower]))
    return value
  quartile_1 = quartile(scores,1)
  quartile_3 = quartile(scores,3)
  scores_vs_label={
      'Low Risk':[],
      'Moderate Risk':[],
      'High Risk':[]
  }
  for score in sorted(scores):
    if score<=quartile_1:
      scores_vs_label['Low Risk'].append(score)
    elif quartile_1<score<quartile_3:
      scores_vs_label['Moderate Risk'].append(score)
    else:
      scores_vs_label['High Risk'].append(score)
  for key,value in scores_vs_label.items():
    if key==label:
      return len(value)
# Input and output handling (do not edit)
print(count_mutation_risk_groups(*literal_eval(input())))
