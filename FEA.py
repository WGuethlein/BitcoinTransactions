def FEA(m, a, k):
    r = 1
    while r < k:
        exponents[r] = (a ** r) % m
        r = r * 2

    answer = 1
    for x in exponents.keys():
        if k - x < 0:
            continue
        
        answer = (answer * exponents[x]) % m

    return answer
