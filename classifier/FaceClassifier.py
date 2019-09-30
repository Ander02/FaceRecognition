import os
import pickle
import numpy as np
from sklearn import neighbors, svm, ensemble

BASE_DIR = os.path.dirname(__file__) + '/'
PATH_TO_PKL = 'trained_classifier.pkl'


class FaceClassifier:
    def __init__(self, model_path=None):

        self.model = None
        if model_path is None:
            return
        elif model_path == 'default':
            model_path = BASE_DIR+PATH_TO_PKL

        # Load models
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)

    def train(self, X, y, model='knn', save_model_path=None):
        if model == 'knn':
            self.model = neighbors.KNeighborsClassifier(3, weights='uniform')
        elif model == 'random_forest':
            self.model = ensemble.RandomForestClassifier(n_estimators=100, max_depth=2)
        else:  # svm
            self.model = svm.SVC(kernel='linear', probability=True)
        self.model.fit(X, y)
        if save_model_path is not None:
            with open(save_model_path, 'wb') as f:
                pickle.dump(self.model, f)

    def classify(self, descriptor):
        if self.model is None:
            print('Train the model before doing classifications.')
            return

        return self.model.predict([descriptor])[0]
