

# importing created functions
from basic_functions import *

# tree is a decision classifier which takes in specific criteria (e.g a string)
# and make a splitter decision.The strategy is to choose the split at each node.
# i.e chooses the "best" split option and “random” to choose the best random split. 

from sklearn import tree

# NumPy can be used as multi-dimensional container of generic data.
# in which data-types can be defined. 

import numpy as np

# stringIO reads and writes strings as files???
from sklearn.externals.six import StringIO
# pydot creates, modifies and process graphs dot language.
#import pydot

## ===================
## 0- Loading the data
## ===================
# calling function to read all cells from data file 
#ramdt = read_file("../project_raw_data/ram.xlsx","all")
ramdt = read_file("../../new_data/ram.xlsx","all")
# calling function to transform row to col
rdtcol = transform_row_to_col(ramdt)

## ===================
## 1- Prepare the data
## ===================
# variable to hold the target data
train_tgt = rdtcol['Type'] 
# variable to hold extracted dataset from row data
# the (extract_ds_from_row_data) function passes the follwing parameters:
# ramdt,range of rows excluding headers,
# range of columns based on index zero (headers) of ramdt.
# (ie. exclude columns[0,1] and include rest of columns.  
# list range 1,12 is cell type 1
# list range 16,19 is cell type 2
# list range 22,64 is cell type 3
# list range 76,113 is cell type 4
train_ds = extract_ds_from_row_data(ramdt,
list(range(1,12)) + list(range(16,19)) + list(range(22,64)) +
list(range(76,113)),range(2,len(ramdt[0])))

#print(train_ds)
#print(train_tgt)

# test data: test the learning on data (the ones we extracted above)
#test_tgt = train_tgt
#test_ds = extract_ds_from_row_data(ramdt,
#list(range(13,15)) + list(range(20,21)) + list(range(65,75)) +
#list(range(114,123)),range(2,len(ramdt[0])))
## ===========
## 2- Learning
## ===========
clf = tree.DecisionTreeClassifier()
clf.fit(train_ds,train_tgt)
## ============================
## 3- test the learning process
## ============================
# We expect the same cell type in test_tgt (truth) and the one predicted by
# the learning
#print (test_tgt) 
#print (clf.predict(test_ds))



## ================================
## 4- visualising the decision tree
## ================================
#dot_data = StringIO();
#tree.export_graphviz(
 #       clf,
  #      out_file=dot_data,
   #     feature_names=ramdt.feature_names,
    #    class_names=ramdt.target_names,
     #   filled=True, rounded=True,
      #  impurity=False);
#graph = pydot.graph_from_dot_data(dot_data.getvalue());
#graph.write_pdf("classification_tree_iris.pdf");

