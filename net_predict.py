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
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler


def run():

    pipeline = Pipeline([
        ('min/max scaler', MinMaxScaler(feature_range=(0.0, 1.0))),
        ('neural network', Classifier(layers=[Layer("ExpLin", units=5), Layer("Softmax")], n_iter=25))])


    X = np.load('All_features.npz')['arr_0']

    all_samples = [1]*141 + [0]*123
    y = np.array(all_samples)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    pipeline.fit(X_train, y_train)
    prediction = pipeline.predict(X_test)
    probs = pipeline.predict_proba(X_test)
    score = pipeline.score(X_test, y_test)

    #print('METRICS SCORE', metrics.accuracy_score(prediction, y_test))

    #nn.fit(X_train, y_train)
    #score = nn.score(X_train, y_train)

    gradation = {1: 5, 0.9: 4, 0.8: 3, 0.7: 2, 0.6: 1}
    res = ''
    for i in probs:
        compare = []
        for u in gradation:
            if i[1] < u:
                compare.append(gradation[u])
        res += str(min(compare)) + ','
    return res


print(run())


#for i in range(10): print(run())

# Sigmoid средняя точность ~ 0,6388 (сильный разброс - 20 :(()
# ExpLin средняя точность ~ 0,667 (не такой сильный разброс - 10 :( )

