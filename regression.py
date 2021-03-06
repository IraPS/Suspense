import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.cross_validation import cross_val_score
from sklearn.preprocessing import MinMaxScaler


def regression(corpus, samples, corpus_devision, test=None):
    X = np.load(corpus + '_features.npz')['arr_0']
    y = np.array(samples)
    scaler = MinMaxScaler()
    # X = scaler.fit_transform(X)


    if corpus_devision is 'auto':
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
        model = LogisticRegression()
        model.fit(X_train, y_train)

        predicted = model.predict(X_test)
        print('Accuracy score is', metrics.accuracy_score(y_test, predicted)*100)

        scores = cross_val_score(LogisticRegression(), X, y, scoring='accuracy', cv=20)
        print('Cross validation accuracy score is', scores.mean()*100)

        for i in range(len(model.coef_[0])):
            print(i+1, model.coef_[0][i])



    else:
        X_train = X
        y_train = y
        X_test = np.load(test + '_features.npz')['arr_0']

    model = LogisticRegression()
    model.fit(X_train, y_train)

    predicted = model.predict(X_test)
    print(predicted)


all_samples = [1]*141 + [0]*123
suspense_samples = [1]*141
unsuspense_samples = [0]*123

regression('All_1', all_samples, 'auto')