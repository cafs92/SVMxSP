import numpy as np
import versus.util as ut



def insertbias(dataset):
    new = []
    for i in range(len(dataset)):
        new.append(np.insert(dataset[i], 0, -1))
    return np.asarray(new)


def dividedata(dataset, trainingsize=0.8):
    np.random.shuffle(dataset)
    trainingSet = dataset[0: int(len(dataset) * trainingsize)]
    testSet = dataset[int(len(dataset) * trainingsize):]
    return trainingSet, testSet


def train(ts ,w, c = 300, eta = 0.1):
    counter = 0
    while counter < c:
        for i in ts:
            u = np.dot(w, i[0:len(i)-1])
            y = np.where(u >= 0.0, 1, 0)
            e = i[len(i) - 1] - y
            w = w + eta*e*i[0:len(i)-1]
        counter += 1
        np.random.shuffle(ts)
    return w


def test(w, vs):
    c = 0
    for i in vs:
        u = np.dot(w, i[0:len(i) - 1])
        y = np.where(u >= 0.0, 1, 0)
        e = i[len(i) - 1] - y
        if e != 0:
            c+=1

    return 1 - (c/len(vs))


def simple_perc(d, c):
    w = np.zeros(d.shape[1])
    D = insertbias(d)
    ts, vs = dividedata(D)
    w = train(ts, w, c)
    error = test(w, vs)
    print(error)

a, b, x1, x2 = ut.new_f()
D = ut.new_d(x1, x2, 2000)
print(D)
c = np.polyfit(x1, x2, 1)
ut.plot(c, D, x1, x2)

simple_perc(D, 100)
