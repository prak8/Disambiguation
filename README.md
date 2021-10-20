# Disambiguation
## Project Information

AIT 526

Programming Assignment II

Author: Team 1 - Alice Chen, Hrishikesh Karambelkar, Prakriti Panday, Sean Park

## Description of the problem to be solved

The objective of the assignment includes building a decision list classifier in order to perform word sense disambiguate and then scoring the performance of the classifier. The training data built a selection of feature vectors via bag of words method. The features were choosen for each sense based on a probability formula that calculated the association of each feature towards each sense based on the training data. The model then is applied towards a test data, where the presense of the feature words disambiguated the target word and returned a score demonstrating the likelihood of that sense's association with the target word.The performance of the classifier on the test data were utlized to build a scorer in order to assess the accuracy of the clasifier. 


## An actual example of program output and usage instructions

The following figures below show the output expected from running this project.  

Decision List: This figure shows the features from the bag of words along with a likihood score.


<img width="703" alt="Screen Shot 2021-10-19 at 7 48 01 PM" src="https://user-images.githubusercontent.com/90986120/138005645-e789ad61-b065-4097-8478-7c74eca984f4.png">



My-Line-Answers: This figure refers to the output from the test data and shows which sense the target word most likely can be associated with.

<img width="711" alt="Screen Shot 2021-10-19 at 7 48 19 PM" src="https://user-images.githubusercontent.com/90986120/138005660-57c78361-17a8-4188-888e-8214b8f7c658.png">


Confusion Matrix: This figure displays the output from running the scorer script on the command line, producing the accuracy score.

<img width="837" alt="Screen Shot 2021-10-19 at 7 44 26 PM" src="https://user-images.githubusercontent.com/90986120/138005675-6c92b39c-cc9e-4edb-8c9d-c1c5a29126d8.png">


Usage instructions

All of the starting files need to be placed in the same folder. These files include the training and testing data, an answer key text file to the test data, also the python script composed for the decision list and the scorer. On the terminal or powershell, navigate to the directory where the file has been stored. Run all the files except the scorer in the initial command, with the output requested to a new text file. If successful initiated, an output should form in the directory, with the output of the decision list script. This output and the answer key can be used to run along with the scorer script to produce the confusion matrix for the accuracy. 

## Algorithm

Description

* Parsing training data for target word.

* With the bag of words method, selection of three words, 2 to the left and 2 to the right, surrounding the target word, in order to build list of features.

* Formulation of the probability for each feature associated with the two sense, product and phone. 

* Classifier applied towards test data, output saved as a text file. 

* Accuracy recorded and a confusion matrix provided in order to measure the performance of the classifier. 

