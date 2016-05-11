import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import roc_curve, auc

train = np.load('train.npz')
train = train['arr_0']
test = np.load('test.npz')
test = test['arr_0']