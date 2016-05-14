import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import roc_curve, auc
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.cross_validation import cross_val_score

X = np.load('all_features.npz')['arr_0']
y = np.array([1]*141 + [0]*123)

#X_test = np.load('new_features.npz')['arr_0']
#print(X_test)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
model = LogisticRegression()
model.fit(X_train, y_train)
#model.fit(X, y)


predicted = model.predict(X_test)
#print(predicted)

'''
mistakes = 0
for i in range(len(y_test)):
    if y_test[i] != predicted[i]:
        #print(y_test[i], predicted[i])
        mistakes += 1
accuracy = ((len(y_test) - mistakes)/len(y_test))*100
'''
print('Accuracy score is', metrics.accuracy_score(y_test, predicted)*100)

scores = cross_val_score(LogisticRegression(), X, y, scoring='accuracy', cv=20)
print('Cross validation accuracy score is', scores.mean()*100)

