def modarray(): 
    
    # too long run time -- solved by pisano period
    
    #  basic idea here: for each m, find the sequence of each Fi(mod(m)) -- until the sequence loop again (until 0, 1 shows up again)

    #  the mod 10 for the sum is still the period sequene -- last digit

    #  follow the squere area

 
    mod_array = [0, 1]

    pre_mod = 0

    cur_mod = 1

    pre_fi = 0 # Fn-1 (F0)

    cur_fi = 1 # Fn (F1)

    while not (pre_mod == 0 and cur_mod == 1 and pre_fi!=0): # while not -- can use three conditions

     # directly use number to represent rather than the array -- find the mod sequence
     # when n = 2

        temp = cur_fi 

        cur_fi = pre_fi + cur_fi # Fn-2 + Fn-1

        next_fi = temp + cur_fi # Fn-1 + Fn

        pre_fi = temp # Fn-1

        pre_mod = cur_mod 

        Fn_sqr = cur_fi * next_fi # (Fn)*(Fn+1)

        cur_mod = Fn_sqr % 10

        mod_array.append(cur_mod)

    return mod_array


def last_digit_Fnsum_sqr(n):

    if n<=1:
        return n

    if n>1:

        mod_array = modarray()
    
        return mod_array[n%(len(mod_array)-2)] # exclude pre_mod -- 0 and cur_mod -- 1 (since the array include pre_mod and cur_mod outside the boundary)


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_Fnsum_sqr(input_n))

#print(last_digit_Fnsum_sqr(1234567890))
