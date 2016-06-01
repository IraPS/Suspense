from all_features import getFeatures
import numpy as np
import pickle

novel = input('Please type the title of the novel which stored in a .txt file: ')
features = getFeatures(novel)
np.savez_compressed(novel + '_features.npz', features)

nn = pickle.load(open('NeuralNet_model.pkl', 'rb'))

D = np.load(novel + '_features.npz')['arr_0']

prediction = nn.predict(D)
probs = nn.predict_proba(D)

simple_predicts = []
scale_predicts = []
for i in prediction:
    simple_predicts.append(i[0])
for i in probs:
    scale_predicts.append(i[1]*10)
    compare = []

print('Simple prediction (suspenseful / unsuspensful) paragraph:\n', simple_predicts, '\n\n')

print('Scale prediction for each paragraph:\n', scale_predicts)
