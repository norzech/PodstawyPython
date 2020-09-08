import numpy as np
from timeit import default_timer
import random
np.random.seed()
A = np.random.randint(0, 1000, 5000)
B = [x for x in range(4999, -1, -1)]


def selectionsort(A):
    for i in range (0, len(A)-1):
        min = i
        for j in range(i+1, len(A)):
            if A[j] < A[min]:
                min = j
        A[i], A[min] = A[min], A[i]
    return A
def bubblesort(A):
    b = True
    while b:
        b = False
        for i in range (0, len(A)):
            for j in range(0, len(A) - 1):
                if A[j] > A[j+1]:
                    A[j], A[j+1] = A[j+1], A[j]
                    b = True
    return A
def countingsort(A):
    n = len(A)
    max = A[0]
    #szukanie maks
    for i in range (0, n):
        if A[i] > max:
            max = A[i]
            i = i + 1
    pom = [0 for x in range(0, max+1)]
    #zliczanie
    for i in range(0, n):
        pom[A[i]] = pom[A[i]] + 1
    k = 0
    for a in range(0, max + 1):
        for b in range(0, pom[a]):
            A[k] = a
            k = k + 1

    return A

    return A

czasy = open ('czasy', 'a')

start = default_timer()
A1 = selectionsort(A)
end = default_timer()
czasy.write("\nselection sort A: \n" + str(end - start))

start = default_timer()
B1 = selectionsort(B)
end = default_timer()
czasy.write("\nselection sort B: \n" + str(end - start))

start = default_timer()
A2 = bubblesort(A)
end = default_timer()
czasy.write("\nbubble sort A: \n" + str(end - start))

start = default_timer()
B2 = bubblesort(B)
end = default_timer()
czasy.write("\nbubble sort B: \n" + str(end - start))

start = default_timer()
A3 = bubblesort(A)
end = default_timer()
czasy.write("\ncounting sort A: \n" + str(end - start))
    
start = default_timer()
B3 = bubblesort(B)
end = default_timer()
czasy.write("\ncounting sort B: \n" + str(end - start))

start = default_timer()
A4 = bubblesort(A)
end = default_timer()
czasy.write("\ndomyslne A: \n" + str(end - start))

start = default_timer()
B4 = bubblesort(B)
end = default_timer()
czasy.write("\ndomyslne B: \n" + str(end - start))
    
