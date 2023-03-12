import numpy as np

def max_pairwise_product(sequence):
    
    sequence_array = np.array(sequence)
    # take the maximum
    max_num = np.max(sequence_array)

    max_index = np.argmax(sequence_array)

    max2nd_squence = np.delete(sequence_array, max_index)
    # by removing the maximum and take 2nd max
    max_2nd_num = np.max(max2nd_squence)

    product = max_num * max_2nd_num

    return product

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split())) 
    # split the input string sequence and re-arrange to a input list
    # map was used for int every string in the input sequence
    print(max_pairwise_product(input_numbers))