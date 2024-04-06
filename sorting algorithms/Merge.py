from random import randint


def main(T,p,r):
    if p < r:
        q = (p+(r-1))//2
        main(T, p, q)
        main(T, q+1, r)
        procedure(T, p, q, r)
    return T

def procedure(T,p,q,r):
    left = q - p + 1
    right = r - q
    L = [0 for _ in range(left)]
    R = [0 for _ in range(right)]

    for i in range(left):
        L[i] = T[p+i]
    for j in range(right):
        R[j] = T[q+j+1]

    i = j = 0
    for k in range(p,r+1):

        if i == left:
            T[k] = R[j]
            j += 1

        elif j == right:
            T[k] = L[i]
            i += 1

        elif L[i] <= R[j]:
            T[k] = L[i]
            i += 1

        elif L[i] > R[j]:
            T[k] = R[j]
            j += 1


T = [randint(1,999) for _ in range(11)]

print(main(T,0,10))
