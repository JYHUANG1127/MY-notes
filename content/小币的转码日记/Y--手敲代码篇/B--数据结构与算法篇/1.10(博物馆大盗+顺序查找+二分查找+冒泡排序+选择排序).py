#动态规划
def thief(items, max_weight):
    # items是宝物列表，每个元素是(重量, 价值)
    # dp[i]表示容量为i时的最大价值
    dp = [0] * (max_weight + 1)
    
    # 遍历每个宝物（0-1背包：先遍历物品）
    for weight, value in items:
        # 逆序遍历容量，避免重复选取
        for i in range(max_weight, weight - 1, -1):
            dp[i] = max(dp[i], dp[i - weight] + value)
    
    return dp[max_weight]

# 宝物列表：(重量, 价值)
treasure = [(2, 3), (3, 4), (4, 8), (5, 8), (9, 10)]
print(thief(treasure, 20)) 
#递归思维
most_value = {}
def Dthief(treasure,weight):
    if treasure == set() or weight == 0:
        most_value[(tuple(treasure),weight)] = 0
        return 0
    elif (tuple(treasure),weight) in most_value:
        return most_value[((tuple(treasure),weight))]
    else:
        vmax = 0
        for t in treasure:
            if t[0] <= weight:
                v = Dthief(treasure-{t},weight-t[0])+ t[1]
                vmax = max(vmax,v)
        most_value[(tuple(treasure),weight)] = vmax
        return vmax
treasure = {(2,3),(3,4),(4,8),(5,8),(9,10)}
print(Dthief(treasure,20))
#顺序查找
def sequential_search(L,num):
    if_find = None
    n = len(L)
    for i in range(n):
        if L[i] == num:
            if_find = i + 1
            break
    return if_find
L = [1,4,6,8,93,6,88,9]
print(sequential_search(L,3)) 
#二分查找
def binary_search(L,num):
    '''
    L:list,and it should be ascending order
    '''
    n = len(L)
    is_find = None
    up = n - 1
    down = 0
    if L[0] > num or L[-1] < num:
        return is_find
    while n:
        i = (up + down)//2
        if L[i] == num:
            is_find = i + 1
        if (L[i] > num and L[i-1] < num) or L[i] == num:
            break
        elif L[i] > num:
            up = i - 1
        else:
            down = i + 1
    return is_find
L = [1,4,6,8,9,67,88,98]
print(binary_search(L,7)) 

def binarySearch(L,num):
    n = len(L)
    up = n - 1
    down = 0
    is_find = None
    while down <= up:
        i = (down + up)//2
        if L[i] == num:
            is_find = i
            break
        elif L[i] > num:
            up = i - 1
        else:
            down = i + 1
    return is_find
#冒泡排序
def bubble_sort(L):
    '''
    return:return L which is ascending order
    '''
    n = len(L)
    i = 0
    j = 1
    z = 1
    while z < len(L):
        while j < n:
            if L[i] > L[j]:
                L[i],L[j] = L[j],L[i]
            i += 1
            j += 1
        i = 0
        j = 1
        z += 1
        n -= 1
    return L
L = [2,25,57,232,6658,987]
print(bubble_sort(L))
#选择排序
def selective_sort(L):
    n = len(L)
    i = 1
    z = 1
    while z < len(L):
        index = 0
        while i < n:
            if L[index] < L[i]:
                index = i
            i += 1
        if index != len(L) - z:
            L[index],L[len(L)-z] = L[len(L)-z],L[index]
        i = 1
        z += 1
        n -= 1
    return L



    