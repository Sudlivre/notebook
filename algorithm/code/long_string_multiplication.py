# Long string multiplication

def big_mul(a, b):
    if not all([a, b]):
        return '0'
    if a == '0' or b == '0':
        return '0'
    la, lb= list(a), list(b)
    la.reverse()
    lb.reverse()
    print(la, lb)
    lc = [0 for _ in range(len(la) + len(lb))]
    for i in range(len(la)):
        for j in range(len(lb)):
            lc[i+j] += int(la[i]) * int(lb[j])
    for index in range(len(lc)):
        if lc[index] > 9:
            lc[index + 1] = lc[index] // 10
            lc[index] = lc[index] % 10
    lc.reverse()
    lc_rev = [str(item) for item in lc]
    c = ''.join(lc_rev)
    return c[1:] if c.startswith('0') else c


print(big_mul('', '33'))
print(big_mul('0', '33'))
print(big_mul('100', '100'))
print(big_mul('999999', '99999'))