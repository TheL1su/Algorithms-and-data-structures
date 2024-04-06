
tab = [5, 10, 1, 0, 90, 3]

def bubble_sort(tab):
   n = len(tab)
   for i in range(n):
       for j in range(0, n-i-1):
           if tab[j] > tab[j+1]:
               tab[j], tab[j+1] = tab[j+1], tab[j]

bubble_sort(tab)
print(tab)
