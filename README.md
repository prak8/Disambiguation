# Disambiguation
## Project Information

AIT 526

Programming Assignment II

Author: Team 1 - Alice Chen, Hrishikesh Karambelkar, Prakriti Panday, Sean Park

## Description of the problem to be solved

The objective of the assignment includes building a decision list classifier in order to perform word sense disambiguate and then scoring the performance of the classifier. The training data built a selection of feature vectors via bag of words method. The features were choosen for each sense based on a probability formula that calculated the association of each feature towards each sense based on the training data. The model then is applied towards a test data, where the presense of the feature words disambiguated the target word and returned a score demonstrating the likelihood of that sense's association with the target word.The performance of the classifier on the test data were utlized to build a scorer in order to assess the accuracy of the clasifier. 


## An actual example of program input and output
Decision List


<img width="703" alt="Screen Shot 2021-10-19 at 7 48 01 PM" src="https://user-images.githubusercontent.com/90986120/138005645-e789ad61-b065-4097-8478-7c74eca984f4.png">



My-Line-Answers

<img width="711" alt="Screen Shot 2021-10-19 at 7 48 19 PM" src="https://user-images.githubusercontent.com/90986120/138005660-57c78361-17a8-4188-888e-8214b8f7c658.png">


Confusion Matrix

<img width="837" alt="Screen Shot 2021-10-19 at 7 44 26 PM" src="https://user-images.githubusercontent.com/90986120/138005675-6c92b39c-cc9e-4edb-8c9d-c1c5a29126d8.png">


## Algorithm

Description

* Parsing training data for target word.

* With the bag of words method, selection of three words, 2 to the left and 2 to the right, surrounding the target word, in order to build list of features.

* Formulation of the probability for each feature associated with the two sense, product and phone. 

* Classifier applied towards test data, output saved as a text file. 

* Accuracy recorded and a confusion matrix provided in order to measure the performance of the classifier. 

