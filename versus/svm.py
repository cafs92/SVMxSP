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
    return cvxopt.matrix([1, 0, 0], [0, 1, 0], [0, 0, 0])


def getq():
    return cvxopt.matrix(np.zeros(3, 1))


def getG(d):
    return cvxopt.matrix((np.concatenate((d[0:len(d) - 1], np.ones((d.shape[0], 1))), axis=1) * d[len(d) - 1]) * -1)


def geth(n):
    return cvxopt.matrix(np.ones(n) * -1)
