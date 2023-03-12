import numpy as np

def max_pairwise_product(sequence):
    products=list()
    # go through all possible product of pairs
    for i in range(len(sequence)):
        for j in range(len(sequence)):
            if sequence[i] != sequence[j]:
                product = sequence[i]*sequence[j]
                products.append(product)
                # solution 2: max_product = max(max_product,
                # numbers[first] * numbers[second])
    products_array = np.array(products)
    return np.max(products_array)

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split())) 
    # split the input string sequence and re-arrange to a input list
    # map was used for int every string in the input sequence
    print(max_pairwise_product(input_numbers))

