import math
import string
import sys

from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.probability import ConditionalFreqDist
from nltk.probability import ConditionalProbDist
from nltk.probability import ELEProbDist
from nltk.tokenize import RegexpTokenizer

training_data = sys.argv[1]
testing_data = sys.argv[2]
training_decision_list = sys.argv[3]

core_word = "line"

decision_list = []


# Function to clean data
def text_clean(input_text):
    input_text = input_text.lower()
    stop_words = stopwords.words("english")
    stop_words.extend(string.punctuation)
    input_text = input_text.replace("lines", "line")
    tokenizer = RegexpTokenizer(r'\w+')
    corpus = tokenizer.tokenize(input_text)
    corpus = [w for w in corpus if w not in stop_words and w != '']
    return corpus

# Function to find nearby words of "line", which is the word we are disambiguating
def find_nearby_words(n, sentence):
    index = sentence.index(core_word)
    nearby_word_index = index + n
    if len(sentence) > nearby_word_index >= 0:
        return sentence[nearby_word_index]
    else:
        return ""

# Function to calculate word frequency of the near by words
def build_conditional_frequency(cond_freq, data, n):
    for element in data:
        sense, context = element['sense'], element['text']
        nearby_word = find_nearby_words(n, context)
        if nearby_word != '':
            condition = nearby_word
            cond_freq[condition][sense] += 1
    return cond_freq


# Function to specify window to be 2 words to the left and 2 words to the right. If match is found in the
# dictionary, return
def find_word_nearby(sentence, rule):
    for i in range(-2, 2):
        if i == 0:
            continue
        word = find_nearby_words(i, sentence)
        if word == rule:
            return word
        
# Function to determine majority sense in the training set
def predict(sentence, majority_label):
    for word in decision_list:
        tag = find_word_nearby(sentence, word[0])
        if tag:
            if word[1] > 0:
                return "phone", tag
            elif word[1] < 0:
                return "product", tag
    return majority_label, "maj_label"


def main():
    # STEP 1: Run using python decision-list.py line-train.xml line-test.xml my-decision-list.txt > my-line-answers.txt
    
    # STEP 2: Build training data
    train_data = []
    with open(training_data, 'r') as data:
        soup = BeautifulSoup(data, 'html.parser')
        for instance in soup.find_all('instance'):
            sentence = dict()
            sentence['id'] = instance['id']
            sentence['sense'] = instance.answer['senseid']
            text = ""
            for s in instance.find_all('s'):
                text = text + " " + s.get_text()
            sentence['text'] = text_clean(text)
            train_data.append(sentence)
            
    # STEP 3: Freq Dist for 2 words before and 2 words after the word "line"
    conditional_freq = ConditionalFreqDist()
    for i in range(-2, 2):
        if i == 0:
            continue
        conditional_freq = build_conditional_frequency(conditional_freq, train_data, i)

    conditional_prob_dist = ConditionalProbDist(conditional_freq, ELEProbDist, 2)
    
    # STEP 4: For Every word selected above, decide phone or product, create a list with the key, probability and sense
    for rule in conditional_prob_dist.conditions():
        phone_probability = conditional_prob_dist[rule].prob("phone")
        product_probability = conditional_prob_dist[rule].prob("product")
        div = phone_probability / product_probability
        if div == 0:
            log_likelihood = 0
        else:
            log_likelihood = math.log(div, 2)
        decision_list.append([rule, log_likelihood, "phone" if log_likelihood > 0 else "product"])
        
    # STEP 5: Sort the decision list in descending order of the absolute value of log-likelihood score
        decision_list.sort(key=lambda rule: math.fabs(rule[1]), reverse=True)

    # STEP 6: Write decision list to a file as required in requirements document
    with open(training_decision_list, 'w') as output:
        for list_item in decision_list:
            output.write('%s\n' % list_item)

    # STEP 7: Read the test data xml
    test_data = []
    with open(testing_data, 'r') as data:
        test_soup = BeautifulSoup(data, 'html.parser')
        for instance in test_soup('instance'):
            sentence = dict()
            sentence['id'] = instance['id']
            text = ""
            for s in instance.find_all('s'):
                text = text + " " + s.get_text()
            sentence['text'] = text_clean(text)
            test_data.append(sentence)

    # STEP 8: Calculate majority sense of training data set. Majority sense is used if no matching words from training
    # data set are found
    sense_phone, sense_product = 0, 0
    for element in train_data:
        if element['sense'] == "phone":
            sense_phone += 1
        elif element['sense'] == 'product':
            sense_product += 1

    majority_sense = "phone" if sense_phone > sense_product else "product"

    # STEP 9: Navigate left and right of the word and find if nearby words are in the training dictionary. If words
    # are present in the sense dictionary from training data, see if they are associated with phone or product
    for element in test_data:
        prediction, tag = predict(element['text'], majority_sense)
        id1 = element['id']
        print(f'<answer instance="{id1}" senseid="{prediction}"/>')


if __name__ == '__main__':
    main()
