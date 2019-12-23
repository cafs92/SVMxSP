import numpy as np
import matplotlib.pyplot as plt


def new_d(x1, x2, d=2):
    D = []
    a, b = -1, 1
    for i in range(d):
        d1 = (b - a) * np.random.rand() + a
        d2 = (b - a) * np.random.rand() + a
        c = getclass(x1, x2, d1, d2)
        D.append([d1, d2, c])
    return np.array(D)

def getclass(x1,x2, d1, d2):
    a = np.array([x1[0], x2[0]])
    b = np.array([x1[1], x2[1]])
    p = np.array([d1, d2])
    a = np.cross(p-a, b-a)
    if a >= 0:
        return 1
    else:
        return -1

def new_f():
    a, b = -1, 1
    x1 = []
    x2 = []
    x1.append((b - a) * np.random.rand() + a)
    x1.append((b - a) * np.random.rand() + a)
    x2.append((b - a) * np.random.rand() + a)
    x2.append((b - a) * np.random.rand() + a)

    c = np.polyfit(x1, x2, 1)
    return c[0], c[1], x1, x2


def plot(c, d, x1, x2):
    polynomial = np.poly1d(c)
    x_axis = np.linspace(-1, 1, 100)
    y_axis = polynomial(x_axis)
    plt.plot(x_axis, y_axis)
    for i in d:
        if i[2] < 0:
            plt.plot(i[0], i[1], 'r*')
        else:
            plt.plot(i[0], i[1], 'bo')
    plt.plot(x1[0], x2[0], 'go')
    plt.plot(x1[1], x2[1], 'go')
    plt.grid('on')
    plt.show()