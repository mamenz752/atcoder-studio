# A.py
X = int(input())

flag = False

if X < 3 or X > 18:
    flag = False
else:
    flag = True

if flag:
    print("Yes")
else:
    print("No")