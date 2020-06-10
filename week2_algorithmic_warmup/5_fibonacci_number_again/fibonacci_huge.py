# Uses python3
# import sys

# calculate the pisano and pisano period
def pisanoPeriod(m):    
    previous = 0
    current = 1
    pisano = [0] 
    for i in range(0, m**2):
        previous, current = current, (previous + current) % m
        # since the period always repeats on 0 and 1
        if previous == 0 and current == 1:
            return i + 1, pisano
        pisano.append(previous)

def fibonacciMod(n, m):
    if m == 1:
        return 0
    # get pisano period and pisano list of m 
    period, pisanoList = pisanoPeriod(m)
   
    #calculate n%period
    n %= period
    # return the answer at index new n of the pisano list
    return pisanoList[n]
    

# if __name__ == '__main__':
#     input = sys.stdin.read();
n, m = map(int, input().split())
print(fibonacciMod(n, m))
