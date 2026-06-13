N = int(input())
S = list(map(str, input().split()))

C = []
for i in range(N):
    c = S[i][0]
    if c == "a" or c == "b" or c == "c":
        C.append("2")
    elif c == "d" or c == "e" or c == "f":
        C.append("3")
    elif c == "g" or c == "h" or c == "i":
        C.append("4")
    elif c == "j" or c == "k" or c == "l":
        C.append("5")
    elif c == "m" or c == "n" or c == "o":
        C.append("6")
    elif c == "p" or c == "q" or c == "r" or c == "s":
        C.append("7")
    elif c == "t" or c == "u" or c == "v":
        C.append("8")
    else:
        C.append("9")

msg = "".join(C)
print(msg)
