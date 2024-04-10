
n = 7
print(n.bit_length()-1)
parent = [-1, 0, 0, 1, 1, 2, 2]
m = n.bit_length() - 1
pa = [[p] + [-1] * m for p in parent]

print(pa)