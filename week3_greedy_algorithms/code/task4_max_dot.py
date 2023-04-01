import numpy as np

def max_dot_product(first_sequence, second_sequence):
    
    dot = 0
    while first_sequence:
        dot=dot+max(first_sequence)*max(second_sequence)
        max_index1 = first_sequence.index(max(first_sequence))
        max_index2 = second_sequence.index(max(second_sequence))
        first_sequence.pop(max_index1)
        second_sequence.pop(max_index2)

    return (dot)

if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))