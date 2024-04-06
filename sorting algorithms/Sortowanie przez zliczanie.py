


def Zliczanie(T,k):
    C = [0] * k
    B = [0] * len(T)

    for i in range(0,len(T)):
        C[T[i]] += 1
    for j in range(1,k):
        C[j] += C[j-1]

    for p in range(len(T)-1,-1,-1):
        B[C[T[p]]-1] = T[p]
        C[T[p]] -= 1
    return B


T = [0, 9, 8, 5, 7, 8, 2, 3, 4, 1, 1, 1, 1, 1, 0]
print(Zliczanie(T,10))