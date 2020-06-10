# Uses python3
def evalt(a, op, b,):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(data):
    def MinMax(i, j):
        minn = float('inf')
        maxx = float('-inf')
        for k in range(i, j):
            a = evalt(M[i][k], op[k - 1], M[k + 1][j])
            b = evalt(m[i][k], op[k - 1], M[k + 1][j])
            c = evalt(M[i][k], op[k - 1], m[k + 1][j])
            d = evalt(m[i][k], op[k - 1], m[k + 1][j])
            minn = min(minn, a, b, c, d)
            maxx = max(maxx, a, b, c, d)
        return minn, maxx

    num, op = [], []
    for i in range(len(data)):
        if i % 2 == 0:
            num.append(int(data[i]))
        else:
            op.append(data[i])
    size = len(num)
    m, M = [], []
    for _ in range(size + 1):
        m.append([0] * (size + 1) )
        M.append([0] * (size + 1) )
    for i in range(1, size + 1):
        m[i][i], M[i][i] = num[i - 1], num[i - 1]
    
    for s in range(1, size):
        for i in range(1, size + 1 - s):
            j = i + s
            m[i][j], M[i][j] = MinMax(i, j)

    return M[1][size]


if __name__ == "__main__":
    print(get_maximum_value(input()))
