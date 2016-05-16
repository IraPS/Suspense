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


def run():
    nn = Classifier(
        layers=[
            Layer("Sigmoid", units=10),
            Layer("Softmax")],
        learning_rate=0.02,
        learning_rule='nesterov',
        n_iter=20)

    X = np.load('All_features.npz')['arr_0']
    all_samples = [1]*141 + [0]*123
    y = np.array(all_samples)

    X_train, X_t, y_train, y_t = train_test_split(X, y, test_size=0.5, random_state=0)
    X_test, X_valid, y_test, y_valid = train_test_split(X_t, y_t, test_size=0.5, random_state=0)


    nn.fit(X_train, y_train)

    y_valid = nn.predict(X_valid)

    score = nn.score(X_test, y_test)

    print('Accuracy is', score)


for i in range(10): run()

# средняя точность ~ 0,6388

