
def selection_sort(T):
    for i in range(len(T)-1):
        min = T[i]
        min_index = i
        for j in range(i+1, len(T)):
            if T[j] < min:
                min = T[j]
                min_index = j
        T[i], T[min_index] = T[min_index], T[i]
    return T

T = [11,12,14,1,2,4]
print(selection_sort(T))