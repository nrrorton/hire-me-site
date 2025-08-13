from collections import defaultdict
from itertools import product

with open(r"C:\Users\nrror\Desktop\Advent of Code\day_4.txt", 'r') as file:
    ls = file.read().strip().split("\n")

boardz = defaultdict(str)
boardz |= {i + 1j * j: x for i, l in enumerate(ls) for j, x in enumerate (l)}
octdir = {i + 1j * j for (i, j) in set(product((-1, 0, 1), (-1, 0, 1))) - {(0, 0)}}

print(
    sum(
        [boardz[z + i *dz] for i in range(4)] == ["X", "M", "A", "S"]
        for z in list(boardz.keys())
        for dz in octdir
    )
)

