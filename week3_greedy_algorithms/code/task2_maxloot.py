from sys import stdin
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

def optimal_value(capacity, weights, values):
    total_value=0
    for i in range(len(weights)): # turns to take goods
        if capacity==0:
            return total_value
        item = best_item(weights, values) # choose which item to pick in this turn; return the index here
        amount_to_take = np.minimum(capacity, weights[item]) # greedy taking all the most valueable goods
        total_value=total_value+amount_to_take*(values[item]/weights[item])
        weights[item]=weights[item]-amount_to_take
        capacity=capacity-amount_to_take

    return total_value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))