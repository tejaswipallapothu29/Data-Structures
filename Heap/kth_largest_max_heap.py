
# code strucure ( pseudo code)

#def heapify(a, n, i):
# take left, take right, and move the node down recursively

#build max heap(a,n):
# for first non leaf node:
#     call heapify
#     decrement, till you reach node

# first given array, try to create max heap from it. then write heapsort logic which should be easy.
#basically you will have to reverse the root and last node and call heapify, decrementing n by 1 each time.

#heapify
a = [-1,20, 15, 18, 8, 10, 5, 17]
n = len(a)
k = 6

def heapify(a,n,i):
    l = 2*i
    r = 2*i+1
    large = i
    c = False
    if l < n and a[l] > a[i]:
        large = l
        c = True
    if r < n and a[r] > a[i]:
        large = r
        c = True
    if c == True:
        if a[r] >= a[l]:
            large = r
        elif a[r] <= a[l]:
            large = l
        c = False
            
    if large != i:
        a[large], a[i] = a[i], a[large]
        heapify(a,n,large)


def build_max_heap(a,n):
    for l in range(n//2-1,0,-1):
        heapify(a,n,l)

def extract_kth_largest(a,n):
    m = a[1]
    a[1] = a[n]
    heapify(a,n,1)

    return m

def kth_largest():
    n = len(a)
    for i in range(k):
        n = n-1
        m = extract_kth_largest(a,n)
    return m
build_max_heap(a,n)
print("max heap is:", a)

print(f"{k}th largest is:",kth_largest())
