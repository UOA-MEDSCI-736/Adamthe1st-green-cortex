

# importing created functions
from basic_functions import *

# tree is a decision classifier which takes in specific criteria (e.g a string)
# and make a splitter decision.The strategy is to choose the split at each node.
# i.e chooses the "best" split option and “random” to choose the best random split. 

from sklearn import tree

# NumPy can be used as multi-dimensional container of generic data.
# in which data-types can be defined. 

import numpy as np

from sklearn.externals.six import StringIO
# pydot creates, modifies and process graphs dot language.
#import pydot

## ===================
## 0- Loading the data
## ===================
# calling function to read all cells from data file   
ramdt = read_file("../project_raw_data/ram.xlsx","all")

# calling function to transform row to col
rdtcol = transform_row_to_col(ramdt)


## ===================
## 1- Prepare the data
## ===================
# creating a variable to hold the target (cell type) data
train_tgt = rdtcol['Type'][0:11] + rdtcol['Type'][15:18] + rdtcol['Type'][21:63] + rdtcol['Type'][75:112]

# train_ds is variable to hold extracted dataset from row data (data we want to train)
# the (extract_ds_from_row_data) function passes the follwing parameters:
# ramdt,range of rows excluding headers,
# range of columns based on index zero (headers) of ramdt.
# (ie. exclude columns[0,1] and include rest of columns.  
# list range 1,12 corresponds to cell type 1
# list range 16,19 corresponds to cell type 2
# list range 22,64 corresponds to cell type 3
# list range 76,113 corresponds to cell type 4

train_ds = extract_ds_from_row_data(ramdt, list(range(1,12)) + list(range(16,19)) + list(range(22,64)) + list(range(76,113)),range(2,len(ramdt[0])))

#loop to print the train data
print("======= Train data ============")
print("Target [Features]")
for i in range(0,len(train_tgt)):
      print(train_tgt[i], train_ds[i])


# test_tgt is variable holding cell type range we want to test.
test_tgt = rdtcol['Type'][11:15] + rdtcol['Type'][19:21] + rdtcol['Type'][64:75] + rdtcol['Type'][113:123]

test_ds = extract_ds_from_row_data(ramdt,
list(range(12,16)) + list(range(19,22)) + list(range(64,76)) +
list(range(113,124)),range(2,len(ramdt[0])))

#loop to print the test data
print("======= Test data ============")
print("Target [Features]")
for i in range(0,len(test_tgt)):
      print(test_tgt[i], test_ds[i])


## ===========
## 2- Learning
## ===========
# fitting the data to the decision tree classifier algorithm 
clf = tree.DecisionTreeClassifier()
clf.fit(train_ds,train_tgt)

## ============================
## 3- test the learning process
## ============================

predicted_tgt = clf.predict(test_ds)

## =======================================
## 4- Compute the accuracy of perdiction
## =======================================

print("======= Prediction ============")
correct = 0
for i in range(0,len(test_tgt)):
      if predicted_tgt[i]  == test_tgt[i]: # when prediction matches with actual
            correct = correct + 1 # increment the correct counter
      print("Actual Cell Type:", test_tgt[i], "Predicted Cell Type:", predicted_tgt[i])

accuracy = correct / len(test_tgt) * 100
print("======= Statistics ============")
print("Accuracy over one run" , round( accuracy , 2), "%")



########### RUNNING 100 TIMES ###################
#this a loop to run the classifier 100 times

accuracy = []
for run in range(0,100):
      ## learn
      clf = tree.DecisionTreeClassifier()
      clf.fit(train_ds,train_tgt)
      ## test
      predicted_tgt = clf.predict(test_ds)
      ## compute
      correct = 0
      for i in range(0,len(test_tgt)):
            if predicted_tgt[i]  == test_tgt[i]: # when prediction matches with actual
                  correct = correct + 1 # increment the correct counter
            
      # calculating accuracty of prediction (%)
      accuracy.append(correct / len(test_tgt) * 100)

# rounding predicted output to the nearest decimal. 
print("Avg. accuracy over 100 runs",round(np.mean(accuracy) , 2) , "%")