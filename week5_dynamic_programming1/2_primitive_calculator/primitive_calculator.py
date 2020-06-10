# Uses python3
import sys

def optimal_sequence(n):
    dp = [0,0]
    track = {1: 0}
    for i in range(2, n + 1):
        one = two = three = None
        # check for possible paths to calculating number i
        if i % 3 == 0:
            three = dp[i//3] + 1
            # print("three:", three)
        if i % 2 == 0:
            two = dp[i//2] + 1
            # print("two:", two)

        one = dp[i - 1] + 1
        # print("one:", one)
        # store the current operation carried out
        temp = 1

        #find the path with minimum operations
        if three:
            if three < one:
                one = three
                temp = 3
        if two:
            if two < one:
                one = two
                temp = 2
        # append the minimum path value(one) into the ith position of dp
        dp.append(one)
        # print("dp:", dp)

        # update track with the previous calculated value before i
        # print("temp:", temp, "\n----------")
        if temp == 1:
            track[i] = i - 1
        else:
            track[i] = i // temp

    # create result by backtracking using track
    result = [n]
    prev = track[n]
    while prev != 0:
        result.append(prev)
        prev = track[prev]
    return result[::-1]

    
input = sys.stdin.read()
n = int(input)
# n = 96234
sequence = optimal_sequence(n)
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
