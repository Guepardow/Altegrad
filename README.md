# Altegrad
Project for Advanced Learning for Text and Graph Data

Link for the report : https://www.overleaf.com/8336378nmwndfjxjxgt#/29534773/

## Organisation
- code : contains all the code (under .py or .ipynb)
- data : contains the original data provided by the challenge
- doc : some articles about email recipients recommendation with the Enron dataset
- results : some intermediate and final resuts

## Structure of the code
There are 3 main Jupyter Notebook
- Structure : explains the structures used in the projet 
- Analysis : explores the data on all the training set
- Prediction and error measure : makes a cross-validation, some predictions, computes the error and write the output

NB : for the moment, the first two are cleaned but the third one is not !

## Models
### Network based algorithms
- random on all users : amongst all {senders + recipients} recommend 10 users randomly for each sender ; 
- random on the past recipients : amongst all {recipients for a sender}, recommend 10 users randomly for each sender ; 
- most frequent recipients : for each sender, recommend the 10 most frequent recipients ; 
- most frequent recipients considering a weighted version : for each sender, recommend 10 recipients using a weighted version of the previous model

### Content based algorithms
- TF-IDF centroids (Carvalho & Cohen) : use TF-IDF with the test-mail and all the documents of the sender to recommend the 10 most similar recipients according to the content of the mail

### Network based + Content based algorithms
- name retrieval and most frequent recipients : search for a name in the content of the mail (first word) and complete the recommendation with, at least, 9 users using the 'most frequent recipients' model

NB : I forget to stemize when I used TD-IDF !

## Difficulties
- How to use cross-validation : if we use temporal CV, we cannot split the data in the training set because some senders with be in the test but will be missig in the train ; if we split the data separatly for each sender, there is a bias between the score computed and the one given by Kaggle ; if we split the data randomly, there is a lower bias.
- Some data are dirty : dates may be year 0001
- beware to the data : lists are not separated with a comma

## Litteracy
Some articles promised a score of 0.5 (the best in the Challenge reached 0.4) and we are currently at 0.34.

For the moment, the best model is the baseline 'most frequent recipients' (score map@10 = 0.34)
