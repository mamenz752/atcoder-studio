# Calculate GCD (最大公約数)
A, B = map(int, input().split())

def gcd(A, B):
    if A > B:
        A = A % B
    else:
        B = B % A
    if A == 0:
        return B
    elif B == 0:
        return A
    else:
        return gcd(A, B)

print(gcd(A, B))