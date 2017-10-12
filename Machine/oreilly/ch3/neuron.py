import numpy as np
import matplotlib.pylab as plt


def step_func(x):
    return np.array(x > 0, dtype=np.int)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


if __name__ == '__main__':
    x = np.arange(-5, 5, 0.1)
    y = sigmoid(x)
    print y
    plt.plot(x, y)
    plt.ylim(-.1, 1.1)
    plt.show()
