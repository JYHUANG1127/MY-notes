#归并排序（利用子列表）
def merge(L1:list,L2:list):
    new_L = []
    first = 0#第一个列表的指针
    second = 0#第二个列表的指针
    n1 = len(L1)
    n2 = len(L2)
    while first < n1 and second < n2:
        if L1[first] > L2[second]:
            new_L.append(L2[second])
            second += 1
        else:
            new_L.append(L1[first])
            first += 1
    if first == n1:
        for i in range(second,n2):
            new_L.append(L2[i])
    if second == n2:
        for i in range(first,n1):
            new_L.append(L1[i])
    return new_L

def merge_sort(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left = merge_sort(L[0:mid])
    right = merge_sort(L[mid:])
    return merge(left,right)

L = [1,22,3,4,4,5,6,7,8,9,34,2,44,32,35,32,532,5532,553,532]
print(merge_sort(L))
#快速排序
def quick_sort(L,start,end):
    if start >= end:
        return L
    index = start
    left = start + 1
    right = end
    while left <= right:
        while left <= right and  L[left] <= L[index]:
            left += 1
        while left <= right and L[right] >= L[index]:
            right -= 1
        if left <= right:
            L[left],L[right] = L[right],L[left]
            left += 1
            right -= 1
    L[index],L[right] = L[right],L[index]
    quick_sort(L,start,right-1)
    quick_sort(L,right + 1,end)
    return L
L1 = [1,22,3,4,4,5,6,7,8,9,34,2,44,32,35,32,532,5532,553,532]
L2 = [6,4,8,2,9,1]
L3 = [3,1,4,1,5,9,2,6,5,3,5]
L4 = [9,8,7,6,5,4,3,2,1]
L5 = [1,2,3,4,5,6,7,8,9]
L6 = [5]
L7 = []
print(quick_sort(L1,0,len(L1) - 1))
print(quick_sort(L2,0,len(L2) - 1))
print(quick_sort(L3,0,len(L3) - 1))
print(quick_sort(L4,0,len(L4) - 1))
print(quick_sort(L5,0,len(L5) - 1))
print(quick_sort(L6,0,len(L6) - 1))
print(quick_sort(L7,0,len(L7) - 1))