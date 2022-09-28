import math
import FEA

def encryption(N, m, e):
    return FEA.FEA(N, m, e)


def decryption(N, c, d):
    return FEA.FEA(N, c, d)


def EEA(a, b):
    r = [a, b]
    q = [None, None]
    x = [1, 0]
    y = [0, 1]

    i = 2
    while True:
        q.append(math.trunc(r[i-2] / r[i-1]))
        r.append(r[i-2] - (q[i] * r[i-1]))
        x.append(x[i-2] - (q[i] * x[i-1]))
        y.append(y[i-2] - (q[i] * y[i-1]))
        if r[i] == 0:
            break
        i = i + 1

    return y[i-1]
