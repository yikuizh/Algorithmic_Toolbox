import numpy as np
# a -while loop for euclim algorithm:
def GCD(a, b):

    n1 = a
    n2 = b
    while np.remainder(n1, n2)!=0:

        a_temp = np.remainder(n1, n2) # replace by remainder

        n1 = n2

        n2 = a_temp

    else:
        return n2
        

if __name__ == '__main__':
    a,b = map(int, input().split())
    print(GCD(a, b))