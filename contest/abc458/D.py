import math
import itertools

X = int(input())
Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]

query = list(itertools.chain.from_iterable(query))
line_item = [X]
for i in range(1, Q * 2, 2):
    line_item.append(query[i - 1])
    line_item.append(query[i])
    half = math.floor(len(line_item) // 2)
    line_item = sorted(line_item)
    median = line_item[half]
    print(median)
