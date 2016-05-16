import sklearn
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import roc_curve, auc
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.cross_validation import cross_val_score
from sknn.mlp import Classifier, Layer
from sklearn.metrics import classification_report


def run():

    nn = Classifier(
        layers=[
            Layer("ExpLin", units=5),
            Layer("Softmax")],
        learning_rate=0.0002,
        learning_rule='nesterov',
        n_iter=50, valid_size=0.1)

    X = np.load('All_features.npz')['arr_0']

    all_samples = [1]*141 + [0]*123
    y = np.array(all_samples)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=0)

    nn.fit(X_train, y_train)

    #y_valid = nn.predict(X_valid)

    score = nn.score(X_test, y_test)

    return score

#print(run())

for i in range(10): print(run())

# Sigmoid средняя точность ~ 0,6388 (сильный разброс - 20 :(()
# ExpLin средняя точность ~ 0,667 (не такой сильный разброс - 10 :( )

