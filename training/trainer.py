from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
from tensorflow import keras

class Trainer:
    """
    Trains a model on training data.
    """

    def __init__(self, model: keras.Model):
        self.model = model
        self.trained = False
    
    def train(self, training_data, holdback: float = 0.1) -> keras.Model:
        """
        Uses training data to train a model.

        Keyword arguments:
        training_data -- The data to be trained on
        holdback -- The amount of training data to use for testing
        """
        # do some training

        # if all goes well, mark as trained and return the model
        self.trained = True
        return self.model