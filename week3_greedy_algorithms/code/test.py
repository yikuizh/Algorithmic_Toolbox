import numpy as np
import numpy as np
def best_item(weights, values):
    max_value_weight=0
    best_item=0
    for i in range(len(weights)):
        if weights[i]>0:
            if values[i]/weights[i]>max_value_weight:
                max_value_weight=values[i]/weights[i]
                best_item=i
    return best_item



first_sequence=[2,3,9]
second_sequence=[7,4,2]

dot = 0
while first_sequence:
    dot=dot+max(first_sequence)*max(second_sequence)
    max_index1 = first_sequence.index(max(first_sequence))
    max_index2 = second_sequence.index(max(second_sequence))
    first_sequence.pop(max_index1)
    second_sequence.pop(max_index2)

print (dot)