#插入排序
def insert_sort(L:list):
    '''
    return: the ascending order of L
    '''
    tail = 0
    n = len(L)
    for cur in range(1,n):
        if L[cur] > L[tail]:
            L.insert(tail + 1,L[cur])
            L.pop(cur + 1)
            tail += 1
            continue
        for j in range(tail + 1):
            if L[cur] < L[j]:
                L.insert(j,L[cur])
                L.pop(cur + 1)
                break
        tail += 1
    return L
L = [5,3,8,2,9,1]
print(insert_sort(L))
#谢尔排序
def gapinsectionsort(L,s,h):
    for i in range(s + h,len(L),h):
        currentvalue = L[i]
        index = i
        while index >= h and L[index - h] > currentvalue:
            L[index] = L[index-h]
            index = index - h
        L[index] = currentvalue
def shell_sort(L:list):
    n = len(L)
    h = n//2#记录间隔
    while h > 0:
        for i in range(h):
            gapinsectionsort(L,i,h)
        h = h // 2
    return L
L = [21,34,354,6,77,88,345,2]
print(shell_sort(L))







