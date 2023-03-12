import numpy as np

def fibonacci_number(n):

    if n<=1:
        return n

    else:
        Fn = np.array(range(n+1))

        Fn[0], Fn[1] = 0, 1

        for i in range(2,n+1):
            Fn[i] = Fn[i-1] + Fn[i-2]

        return Fn[n-1]+Fn[n-2] 


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))