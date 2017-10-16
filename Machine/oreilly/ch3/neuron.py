import numpy as np
import matplotlib.pylab as plt


def step_func(x):
    return np.array(x > 0, dtype=np.int)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


def soft_max(x):
    c = np.max(x)
    exp_x = np.exp(x - c)
    sum_x = np.sum(exp_x)
    y = exp_x / sum_x
    return y


def first_layer():
    x = np.array([1, 0.5])
    w1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    b1 = np.array([.1, .2, .3])

    return np.dot(x, w1) + b1


if __name__ == '__main__':
    a1 = first_layer()
    print sigmoid(a1)
