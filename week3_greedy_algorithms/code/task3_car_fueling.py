from sys import stdin
import numpy as np

def min_refills(distance, tank, stops):

    num_refill=0
    stop = 0

    while (distance-stop) > tank:
        temp_stops=[]
        for i in range(len(stops)):
            if stops[i]<=(stop + tank) and stops[i]>stop:
                temp_stops.append(stops[i])
        if not temp_stops:
            return (-1)
            break
        else:
            stop = np.max(temp_stops)
            num_refill+=1
        
    return num_refill
            

if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops)) # distance is d; tank is m; stops is a squence