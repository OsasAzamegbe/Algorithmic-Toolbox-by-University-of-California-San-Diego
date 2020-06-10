# Uses python3
import sys

def get_change(m):
    #write your code here
    ans = 0
    
    while m // 10 >= 1:
        ans += 1
        m  -= 10
    while m // 5 >= 1:
        ans += 1
        m -= 5
    if m > 0:
        ans += m
        
    return ans

# if __name__ == '__main__':
#     m = int(sys.stdin.read())
m = int(input())
print(get_change(m))
