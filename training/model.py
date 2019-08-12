from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
from tensorflow import keras

class DocLabellingModel:
    """
    Creates a keras model specifically for labelling
    """

    def __init__(self, labels: int, vocab_size: int = 10000):
        self.model = keras.Sequential([
            keras.layers.Embedding(vocab_size, 16),
            keras.layers.GlobalAveragePooling1D(),
            keras.layers.Dense(16, activation=tf.nn.relu),
            keras.layers.Dense(labels, activation=tf.nn.sigmoid)
        ])
