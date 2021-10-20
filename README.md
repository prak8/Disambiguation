# Disambiguation
## Project Information

AIT 526

Programming Assignment 2

Author: Team 1 - Alice Chen, Hrishikesh Karambelkar, Prakriti Panday, Sean Park

## Description of the problem to be solved

The objective of the assignment is to (1) build a decision list classifier to disambiguate word sense and (2) develop a scorer to determine the performance of the classifier. In the test data, a list of sentences is provided with the target word “line” where its sense could be “phone” or “product”.  The model builds a selection of feature vectors via the bag of words method. The features are chosen for each sense based on its location, which is two to the left and two to the right of the target word. A log-likelihood score is determined for each feature and its sense. Using the log-likelihood score, the model is applied to the test data, where the presence of the feature words is used to disambiguate the target word. Finally, a scorer is developed to assess the accuracy of the classifier on the test data.  The scorer takes the sense predicted by the model and compares it to the gold standar key to assess the accuracy using a confusion matrix.


## An actual example of program output and usage instructions

The following figures below show the output expected from running this project.  

Decision-List: This figure shows the features from the bag of words along with a log-likelihood score.


<img width="703" alt="Screen Shot 2021-10-19 at 7 48 01 PM" src="https://user-images.githubusercontent.com/90986120/138005645-e789ad61-b065-4097-8478-7c74eca984f4.png">



My-Line-Answers: This figure refers to the output from the test data and shows which sense the target word most likely can be associated with.

<img width="711" alt="Screen Shot 2021-10-19 at 7 48 19 PM" src="https://user-images.githubusercontent.com/90986120/138005660-57c78361-17a8-4188-888e-8214b8f7c658.png">


Confusion Matrix: This figure displays the output from running the scorer script on the command line, producing the accuracy score.

<img width="837" alt="Screen Shot 2021-10-19 at 7 44 26 PM" src="https://user-images.githubusercontent.com/90986120/138005675-6c92b39c-cc9e-4edb-8c9d-c1c5a29126d8.png">


Usage instructions

All of the following files need to be placed in the same directory as the decision-list.py and scorer.py:
  -  line-train.xml (training data)
  -  line-test.xml (test data)
  -  line-answers.txt (answer key) 
On the terminal or powershell, navigate to the directory where the file has been stored. Execute the script by entering: 
    python decision-list.py line-train.xml line-test.xml my-decision-list.txt > my-line-answers.txt
If the script is executed successfully, two output files will generate: my-decision-list.txt and my-line-answers.txt 
To execute with the scorer.py script, navigate to the same directory where the files are stored and enter the following: 
    python scorer.py my-line-answers.txt line-answers.txt
If the script is executed successfully, the model accuracy percentage, the baseline accuracy percentage and the confusion matrix appear on the screen.  

## Algorithm

Description

* Parsing training data for target word.

* With the bag of words method, selection of three words, 2 to the left and 2 to the right, surrounding the target word, in order to build list of features.

* Formulation of the probability for each feature associated with the two sense, product and phone. 

* Classifier applied towards test data, output saved as a text file. 

* Accuracy recorded and a confusion matrix provided in order to measure the performance of the classifier. 

Figure below shows a flow diagram




![Untitled Document](https://user-images.githubusercontent.com/90986120/138015263-3ab6dda6-c4e2-4616-be30-2453544b013e.png)

