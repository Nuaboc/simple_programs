# Neuron

import numpy as np


def sigmoid(x):
    # Our activation function: f(x) = 1 / ( 1 + e^(-x))
    return 1 / (1 + np.exp(-x))
