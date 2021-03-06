from asreviewcontrib.models.model_switcher import base_switcher

from asreviewcontrib.models.cnn import POWER_CNN
from asreview.models.classifiers.svm import SVMClassifier


class SVM_CNN_Model(base_switcher):

    name = "svm_cnn"

    def __init__(self):
        super().__init__()
        self._model_1 = SVMClassifier()
        self._model_2 = POWER_CNN(verbose=0)
