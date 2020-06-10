# Uses python3
import sys
# from operator import itemgetter
def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    size = len(weights)
    frac = [[float(values[i]/weights[i]), weights[i]] for i in range(size)]
    frac.sort(key=lambda item: item[0], reverse=True)
    # frac.sort(key=itemgetter(0), reverse=True)

    for i in range(size):
        if capacity == 0:
            return value
        a = min(capacity, frac[i][1])
        value += float(a * frac[i][0])
        frac[i][1] -= a
        capacity -= a        
        

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
