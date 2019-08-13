from __future__ import absolute_import, division, print_function, unicode_literals

from typing import List

import tensorflow as tf
from tensorflow import keras

class Trainer:
    """
    Trains a model on training data.
    """

    def __init__(self, model: keras.Model):
        self.model = model
    
    def train(self, x_train, y_train, holdback: float = 0.1) -> keras.Model:
        """
        Uses training data to train a model.

        Keyword arguments:
        x_train -- Input training data
        y_train -- Results training data
        holdback -- The amount (as a percentage) of training data to use for validation
        """
        if len(x_train) != len(y_train):
            raise "Training data must be of the same size"
        total_train_len = len(x_train)
        partial_index = int(total_train_len - (total_train_len * holdback))

        partial_x_train = x_train[:partial_index]
        partial_y_train = y_train[:partial_index]

        x_validation = x_train[partial_index:]
        y_validation = y_train[partial_index:]

        self.model.fit(
            partial_x_train,
            partial_y_train,
            epochs=40,
            validation_data=(x_validation, y_validation)
        )

        return self.model

    def evaluate(self, x_eval, y_eval):
        return self.model.evaluate(x_eval, y_eval)