#!/usr/bin/env python
import sys
import math
from tabulate import tabulate

def truncate_float(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

def eij_func(i,j,eij_array):
    minimum = 0
    root = 0
    for r in range(i,j+1): #j+1 because it is not inclusive, to include j itself we add 1 to the range
        wert = 0
        if r+1 < len(eij_array) and j < len(eij_array):
            wert += eij_array[r+1][j]
        if r-1 >= 0 and r-1 < len(eij_array) and i < len(eij_array):
            wert += eij_array[i][r-1]
        if minimum == 0 or minimum > wert:
            minimum = wert
            root = r
    return (minimum,root)

try:
    keys = raw_input("Keys (ex. [1,2,3,4,5]): ")
    if not keys:
        raise ValueError('[X] Empty Key List')
    probs = raw_input("Probabilities (ex. [0.2,0.1,0.5,0.1,0.1]): ")
    if not probs:
        raise ValueError('[X] Empty Probabilities List')
except KeyboardInterrupt,k:
    print("\nCya!")
    sys.exit(1)
except ValueError,e:
    print(e)
    sys.exit(1)

keys = eval(keys)
probs = eval(probs)

if len(keys) != len(probs):
    print("[X] Keys and Probabilities do not match in length: " + str(len(keys)) + " " + str(len(probs)))
    sys.exit(1)

if all(isinstance(prob, float) for prob in probs):
   if float(truncate_float(sum(probs),1) ) != 1.0:
       print("[X] Probabilities must sum up to 1.0.")
       sys.exit(1)
else:
   print("[X] Probabilities must be of type float")
   sys.exit(1)

print("[i] Everything ok! Generating Tables...\n")

wij = []
eij = []

index = 0
for key in keys:
    row = []
    res = 0
    eij.append([0] * len(keys))
    for prob in probs[:index]: #zero out everything to the starting index
        row.append(0)
    for prob in probs[index:]: #calculate everything from the index to the end
        res += prob
        row.append(res)
    wij.append(row)
    index += 1
wij_result = tabulate(wij, headers=keys, tablefmt='orgtbl')

print("[w]ij:\n" + wij_result + "\n")

print("[i] Roots: \n")
diff = 0
for prob in probs:
    i = 0
    for prob in probs:
        j = i + diff
        result = eij_func(i,j,eij)
        (minimum,root) = result
        if i < len(eij) and j < len(wij):
            if i != j and root < len(keys) and i < len(keys) and j < len(keys):
                print("[" + str(keys[i]) + " to " + str(keys[j]) + "] = " + str(keys[root]))
            eij[i][j] = wij[i][j] + minimum
        i += 1
    diff += 1

print("\n")
eij_result = tabulate(eij, headers=keys, tablefmt='orgtbl')
print("[e]ij:\n" + eij_result + "\n")
