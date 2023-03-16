import numpy as np

def hugeFi(n,m): # version to avoid RuntimeWarning: overflow encountered in long_scalars
# too long run time -- solved by pisano period
    if n<=1:
        return n
    # no need a else here
    pre_mod = 0

    cur_mod = 1

    for _ in range(n-1): # directly use number to represent rather than the array
        temp = pre_mod
        
        pre_mod = Fn + Fn_1
        
        Fn = temp

    return  Fn_1 % m


if __name__ == '__main__':
    n,m = map(int, input().split())
    print(hugeFi(n, m))