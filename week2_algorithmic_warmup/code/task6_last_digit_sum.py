import numpy as np

def modarray(n): # version to avoid RuntimeWarning: overflow encountered in long_scalars
    
    # too long run time -- solved by pisano period
    
    #  basic idea here: for each m, find the sequence of each Fi(mod(m)) -- until the sequence loop again (until 0, 1 shows up again)
    #  the mod 10 for the sum is still the period sequene -- last digit
    # no need a else here
    mod_array = [0, 1]

    pre_mod = 0

    cur_mod = 1

    pre_fi = 0

    cur_fi = 1

    sum = 1

    while not (pre_mod == 0 and cur_mod == 1 and pre_fi!=0): # while not -- can use three conditions

     # directly use number to represent rather than the array -- find the mod sequence
      
        temp = cur_fi

        cur_fi = pre_fi + cur_fi 

        pre_fi = temp

        pre_mod = cur_mod

        sum = cur_fi + sum

        cur_mod = sum % 10

        mod_array.append(cur_mod)

    return mod_array

def last_digit_Fnsum(n):

    if n<=1:
        return n

    mod_array = modarray(n)
    
    return mod_array[n%(len(mod_array)-2)] # exclude pre_mod -- 0 and cur_mod -- 1 (since the array include pre_mod and cur_mod outside the boundary)


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_Fnsum(input_n))

