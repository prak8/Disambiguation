import sys
import nltk
import pandas as pd
import scipy
from nltk.metrics import ConfusionMatrix

my_answers = sys.argv[1]
line_answers = sys.argv[2]

# STEP 1: Run using python scorer.py my-line-answers.txt line-answers.txt
    
# STEP 2: Bring in the output file "my-line-answers.txt". Separate line and sense ID and create a dictionary.  
with open(my_answers, 'r') as myanswers: 
    myans = [line.rstrip('\n') for line in myanswers] 
    my = [i.split(':"', 1) for i in myans] 
    predicted = {} 

    for a in range (1,len(my)): 
        key=my[a][0]
        value=my[a][1]
        predicted[key]=value
  
    myans_list=[]                   
    for v in predicted:
        myans_list.append(predicted[v])
        
# STEP 3: Bring in the test key "line-answers.txt". Separate line and sense ID and create a dictionary.          
with open(line_answers, 'r') as goldstandard: 
    goldstand = [line.rstrip('\n') for line in goldstandard] 
    gold= [i.split(':"', 1) for i in goldstand] 
    observed = {} 

    for a in range (1,len(gold)): 
        key=gold[a][0]         
        value=gold[a][1]       
        observed[key]=value
   
    gold_list=[]
    for v in observed:
        gold_list.append(observed[v])

# STEP 4: Generate a confusion matrix by comparing the output answers with the gold standard key answers.
ConfMatrix = ConfusionMatrix(gold_list,myans_list) 
x = 0
for i in range(len(myans_list)):
    if myans_list[i] == gold_list[i]: 
        x += 1

# STEP 5: Calculate the model accuracy
accuracy = (x/len(myans_list)*100)

# STEP 6: Calculate the baseline accuracy using only majority sense
product_count = myans_list.count(' senseid="product"/>')
baseline_accuracy = (product_count/len(myans_list)*100)
                             
print('Accuracy of the classifier is:',accuracy,'\n\n''Baseline Accuracy is:',baseline_accuracy,'\n\n''Confusion Matrix: ',str(ConfMatrix),)