def encryption(N, m, e):
    return FEA(N, m, e)


def decryption(N, c, d):
    return FEA(N, c, d)


def EEA(a, b):
    r = [a, b]
    q = [None, None]
    x = [1, 0]
    y = [0, 1]

    i = 2
    while r[i] != 0:
        q[i] = r[i-2] / r[i-1]
        r[i] = r[i-2] - (q * r[i-1])
        x[i] = x[i-2] - (q * x[i-1])
        y[i] = y[i-2] - (q * y[i-1])

    return y[i-1]
