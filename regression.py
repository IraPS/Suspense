import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import roc_curve, auc
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.cross_validation import cross_val_score

X = np.load('all_features.npz')['arr_0']
y = np.array([0]*28 + [1]*136)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
model = LogisticRegression()
model.fit(X_train, y_train)


predicted = model.predict(X_test)

for i in range(len(y_test)):
    print(predicted[i], y_test[i])

scores = cross_val_score(LogisticRegression(), X, y, scoring='accuracy', cv=20)
print(scores)
print(scores.mean())