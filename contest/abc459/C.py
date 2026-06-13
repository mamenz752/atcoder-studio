import array
import sys


input = sys.stdin
N, Q = map(int, input.readline().split())

query = array.array("i", [0] * (Q * 2))
query = [list(map(int, input.readline().rstrip().split())) for _ in range(Q)]

masu = array.array("i", [0 for _ in range(N)])

def all_masu_one(masu):
    for i in range(N):
        if masu[i] < 1:
            return 0
    return 1

K = 0
for i in range(Q):
    if query[i][0] == 2:
        K = K + 1

for t, z in query:
    if t == 1:
        masu[z - 1] = masu[z - 1] + 1
        zero = all_masu_one(masu)
        if zero == 1:
            masu = [a - 1 for a in masu]
    elif t == 2:
        count = 0
        for j in range(N):
            if masu[j] >= z:
                count = count + 1
        print(count)


# import sys

# input=sys.stdin.readline
# N,Q=map(int,input().split())
# query=[list(map(int,input().split())) for _ in range(Q)]
# grid=[0]*(N+1)

# box_count_dict=[0]*(Q+2)
# box_count_dict[0]=N

# cum_count=[N]*(Q+2)

# erased_amount=0
# checker=0

# for t,z in query:
#     if t==1:
#         cum_count[grid[z]]-=1
        
#         grid[z]+=1
#         box_count_dict[grid[z]]+=1
#         box_count_dict[grid[z]-1]=max(0,box_count_dict[grid[z]-1]-1)

#         if box_count_dict[checker]==0:
#             checker+=1
#             erased_amount+=1

#     elif t==2:
#         target_internal=z+erased_amount-1
#         if target_internal<0:
#             print(N)
#         elif target_internal<=Q:
#             print(N-cum_count[target_internal])
#         else:
#             print(0)
