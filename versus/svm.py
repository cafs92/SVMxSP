import cvxopt
import numpy as np

def qp(d):
    r, c = d.shape
    P = cvxopt.matrix([1, 0, 0], [0, 1, 0], [0, 0, 0])
    q = cvxopt.matrix(np.zeroes(r))
    G = cvxopt.matrix() * -1
    h = cvxopt.matrix(np.ones(r) * -1)
    s = cvxopt.solvers.qp(P, q, G, h)
    return s['x']

