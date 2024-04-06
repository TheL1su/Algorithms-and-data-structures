
def left(i): return 2*i+1
def right(i): return 2*i+2
def parent(i): return (i-1)//2

def heapify(Tab,n,i):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and Tab[l] < Tab[max_ind]:
        max_ind = l
    if r < n and Tab[r] < Tab[max_ind]:
        max_ind = r
    if max_ind != i:
        Tab[i],Tab[max_ind] = Tab[max_ind],Tab[i]
        heapify(Tab,n,max_ind)

def build_heap(Tab):
    n = len(Tab)
    for i in range(parent(n-1),-1,-1):
        heapify(Tab,n,i)

def heapsort(Tab):
    n = len(Tab)
    build_heap(Tab)
    for i in range(n-1,0,-1):
        Tab[0],Tab[i] = Tab[i],Tab[0]
        heapify(Tab,i,0)
    return Tab[::-1]

T = [1,7,-1,2,3,-2,-8,10,12,4]

print(heapsort(T))