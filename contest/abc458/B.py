H, W = map(int, input().split())

masu = []

if H == 1 and W == 1:
    print(0)
else:
    for i in range(1, H+1):
        masu_line = []
        for j in range(1, W+1):
            masu_num = i + j
            count = 4
            if i - 1 < 1:
                count -= 1
            if i + 1 > H:
                count -= 1
            if j - 1 < 1:
                count -= 1
            if j + 1 > W:
                count -= 1
            masu_line.append(count)
        masu_line = [str(i) for i in masu_line]
        masu_line = " ".join(masu_line)
        masu.append(masu_line)
    print("\n".join(masu))