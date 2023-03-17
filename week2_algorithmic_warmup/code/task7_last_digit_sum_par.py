def modarray(): # version to avoid RuntimeWarning: overflow encountered in long_scalars
    
    # too long run time -- solved by pisano period
    
    #  basic idea here: for each m, find the sequence of each Fi(mod(m)) -- until the sequence loop again (until 0, 1 shows up again)
    #  the mod 10 for the sum is still the period sequene -- last digit
    #  partial sum (Fn+..+..Fm) == (sum(Fn) - sum(Fm-1)) % 10 = sum(Fn)%10 - sum(Fm-1)%10
 
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

def last_digit_Fnsum_par(m, n): # three types of case to consider

    if m<=1 and n<=1:
        return n-m

    if m<=1 and n>1:

        mod_array = modarray()

        n_mod = mod_array[n%(len(mod_array)-2)]

        # m_mod = mod_array[m%(len(mod_array)-2)]

        return n_mod

    if m>1 and n>1:

        m_mod = m-1

        mod_array = modarray()

        n_mod = mod_array[n%(len(mod_array)-2)] 
        
        m_mod = mod_array[(m-1)%(len(mod_array)-2)] # mod of sum until Fm-1 not Fm

        if n_mod >= m_mod:
            return abs(n_mod - m_mod)
        
        if n_mod < m_mod:
            return (n_mod+10) - m_mod
    
         # exclude pre_mod -- 0 and cur_mod -- 1 (since the array include pre_mod and cur_mod outside the boundary)

if __name__ == '__main__':
    m,n = map(int, input().split()) # m <= n
    print(last_digit_Fnsum_par(m, n))
#print(last_digit_Fnsum_par(5, 10))