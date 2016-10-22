

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
ramdt = read_file("../project_raw_data/ram.xlsx","all")

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
# range of columns based on index zero of ramdt (headeres)
# (ie. exclude columns[0,1] and include rest of columns.  
train_ds = extract_ds_from_row_data(ramdt,
list(range(1,5)) + list(range(10,15)),   
 range(2,len(ramdt[0])))

print(train_ds)

## ===========
## 2- Learning
## ===========
#clf = tree.DecisionTreeClassifier();
#clf.fit(train_ds,train_tgt);


