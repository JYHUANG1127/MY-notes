import time
def bubble_sort(L):
    t0 = time.perf_counter()
    did_swap = True
    while did_swap:
        did_swap = False
        for i in range(1,len(L)):
            if L[i-1] > L[i]:
                did_swap = True
                (L[i-1],L[i])=(L[i],L[i-1])
    dt = time .perf_counter() - t0
    print("排序时间为：",dt)
    return L
L1=[10086,2342,8734,78,345,887,90054,22356,3524]
bubble_sort(L1)
print(L1)
#只要发生了交换，就会吧did_swap设置为True，然后进行下一轮比较，一旦没有发生交换，did_swap就是False，while循环就跳出了

import time
def selection_sort(L):
    t0 = time.perf_counter()
    for i in range(len(L)):
        for j in range(i,len(L)):
            if  L[j] <L[i]:
                L[i],L[j]=L[j],L[i]
    dt = time.perf_counter()-t0
    print("排序时间为：",dt)
    return print(L)
L2=[10086,2134,346,5657,6,87,53467,8768,2323]
selection_sort(L2)
#第一轮循环找到应该在第一个位置的元素，第二轮循环找到应该在第二个位置的元素，依次类推，每一轮循环都是这个位置的值与剩下的所有元素的大小比较

import time
def selection_sort_var(L):
    t0 = time.perf_counter()
    for i in range(len(L)):
        smallest = L[i]
        smallest_index = i
        for j in range(i,len(L)):
            if L[j] < smallest:
                smallest = L[j]
                smallest_index = j
        L[i],L[smallest_index] = L[smallest_index],L[i]
    dt = time.perf_counter()-t0
    print("排序时间为：",dt)
    return print(L)
L3=[34325,32545,7,88,5,2,2235,7688,876,443,4355,43]   
selection_sort_var(L3)