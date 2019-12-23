import cvxopt
import numpy as np

def qp(d):
    r, c = d.shape
    P = getP()
    q = getq()
    G = getG(d)
    h = geth(r)
    s = cvxopt.solvers.qp(P, q, G, h)
    return s['x']

def getP():
    return cvxopt.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 0]], tc='d')


def getq():
    return cvxopt.matrix(np.zeros((3, 1)))


def getG(d):
    aux = np.concatenate((d[:, 0:d.shape[1] - 1], np.ones((d.shape[1], 1))), axis=1)
    return cvxopt.matrix((aux * np.array(d[d.shape[1] - 1], ndmin=2).T) * -1)


def geth(n):
    return cvxopt.matrix(np.ones(n) * -1)
