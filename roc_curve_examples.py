
# Starting code for this example is taken from here: https://www.statology.org/plot-roc-curve-python/

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import matplotlib.pyplot as plt

# Import dataset from CSV file on Github
url = "https://raw.githubusercontent.com/Statology/Python-Guides/main/default.csv"
data = pd.read_csv(url)

# Define the predictor variables and the response variable
X = data[['student', 'balance', 'income']]
y = data['default']

# Ssplit the dataset into training (70%) and testing (30%) sets
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0) 

# Instantiate the model
log_regression = LogisticRegression()

# Fit the model using the training data
log_regression.fit(X_train,y_train)

# Define metrics
y_pred_proba = log_regression.predict_proba(X_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)

# Compute AUC
auc = metrics.roc_auc_score(y_test, y_pred_proba)

# Create ROC curve and add AUC info
plt.plot(fpr,tpr,label="AUC="+str(auc))
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend(loc=4)
plt.show()


# Now let's plot ROC curve from scratch using only y_test and y_pred_proba

# Create a grid of values under which the curve will be computed
grid = np.arange(0, 1, 0.001)
grid_n = len(grid)

fpr_for_roc = np.empty([grid_n])  # FPR values array
tpr_for_roc = np.empty([grid_n])  # TPR values array


for i in range(grid_n):
    element = grid[i]
    tp_n = np.sum((y_pred_proba > element) & (y_test == 1))
    fn_n = np.sum((y_pred_proba <= element) & (y_test == 1))
    fp_n = np.sum((y_pred_proba > element) & (y_test == 0))
    tn_n = np.sum((y_pred_proba <= element) & (y_test == 0))

    print(f'Level {element}: TP {tp_n}, FN {fn_n}, FP {fp_n}, TN {tn_n}')

    tpr_n = tp_n/(tp_n+fn_n)
    fpr_n = fp_n/(fp_n+tn_n)

    print(f'Level {element}: TPR {tpr_n}, FPR {fpr_n}')

    tpr_for_roc[grid_n-i-1] = tpr_n
    fpr_for_roc[grid_n-i-1] = fpr_n

print(f'FPR for ROC: {fpr_for_roc}')
print(f'TPR for ROC: {tpr_for_roc}')

# This is the AUC
auc = np.trapz(tpr_for_roc, fpr_for_roc)

# Plotting
plt.plot(fpr_for_roc, tpr_for_roc, label="AUC approx="+str(auc))
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend(loc=4)
plt.show()


# One more useful tutorial https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-classification-in-python/
