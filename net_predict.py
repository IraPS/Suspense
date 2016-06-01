import numpy as np
from sklearn.cross_validation import train_test_split
from sknn.mlp import Classifier, Layer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
import pickle



def predict():

    pipeline = Pipeline([
        ('min/max scaler', MinMaxScaler(feature_range=(0.0, 1.0))),
        ('neural network', Classifier(layers=[Layer("ExpLin", units=5), Layer("Softmax")], n_iter=25))])

    X = np.load('All_features.npz')['arr_0']

    D = np.load('Akunin_features.npz')['arr_0']

    all_samples = [1]*141 + [0]*123
    y = np.array(all_samples)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.0, random_state=0)

    pipeline.fit(X_train, y_train)
    pickle.dump(pipeline, open('NeuralNet_model.pkl', 'wb'))
    prediction = pipeline.predict(D)
    probs = pipeline.predict_proba(D)

    gradation = {1.01: 5, 0.9: 4, 0.8: 3, 0.7: 2, 0.6: 1}
    ress1 = []
    simple_predicts = []
    scale_predicts = []
    for i in prediction:
        simple_predicts.append(i[0])
    for i in probs:
        scale_predicts.append(i[1]*10)
        compare = []
        for u in gradation:
            if i[1] < u:
                compare.append(gradation[u])
        ress1.append(min(compare))

    return simple_predicts, scale_predicts


#print(predict())
