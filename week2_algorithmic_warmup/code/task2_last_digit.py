import numpy as np

def last_digit_Fn(n):
    if n<=1:
        return n

    else:
        # fisrt create the F60 sequence -- 60 as a cycle
        Fn = np.array(range(60))

        Fn[0], Fn[1] = 0, 1

        for i in range(2,60):
            Fn[i] = Fn[i-1] + Fn[i-2]

        remainder = np.remainder(n, 60) 
        digit = Fn[remainder]%10 # calculate the last digit
        return digit



if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_Fn(input_n))