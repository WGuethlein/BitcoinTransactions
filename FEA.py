def FEA(m, a, k):
    r = 1
    exponents = []
    while r < k:
        exponents.append((a ** r) % m)
        r = r * 2

    answer = 1
    x = len(exponents)
    while True:
        if x == 0:
            break
        #print("exp:")
        #print(exponents[x-1])
        #print(k)
        #print(2 ** (x-1))
        #print(k-exponents[x-1])
        if k - (2 ** (x-1)) < 0:
            x = x - 1
            continue
        
        answer = (answer * exponents[x-1]) % m
        #print("ans")
        #print(answer)
        k = k -(2 ** (x-1))
        x = x - 1
    print(answer)
    return answer
