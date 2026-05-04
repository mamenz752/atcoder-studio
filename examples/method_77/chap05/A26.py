# Prime Check (素数判定)
import math

Q = int(input())
X = list(int(input()) for _ in range(Q))

for x in X:
    flag = True
    sqrt = math.floor(math.sqrt(x))
    for i in range(2, sqrt + 1):
        if x % i == 0:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")