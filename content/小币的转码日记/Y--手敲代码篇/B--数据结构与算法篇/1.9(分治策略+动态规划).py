#分治策略解决找零钱的问题
#贪心策略
def gre_MC(num:int):
    changer_list = [100,50,20,10,5,1]
    changer_num = 0
    for i in changer_list:
        x = num // i
        y = num % i
        changer_num += x
        num = y
    return changer_num
print(gre_MC(15))
#递归策略
best_num ={}#key:金额 value：该金额的最小硬币数
def recMC(L,num):
    '''
    L:list,all kinds of changer,need to be in ascending order
    num:the number that you need to make changer
    '''
    if num in best_num:
        x = best_num[num]
        return x
    elif num in L:
        best_num[num] = 1
        return 1
    elif num < L[0]:
        best_num[num] = num
        return num
    else:
        min_coins = float('inf')
        for i in L:
            if i <= num:
                current_coins = recMC(L,num - i) + 1
                if current_coins < min_coins:
                    min_coins = current_coins
        best_num[num] = min_coins
        return min_coins
L = [1,5,10,25]
recMC(L,63)
print(best_num[63])
#在写递归函数时，一定要先写结束条件，也就是可以直接返回值的情况，通常是把问题分成了最小值的情况，但也有例外，比如上面的num已经储存在了best_num中
#然后是什么时候要调用自身，记住这个时候需要假装下一层的函数工作已经完成了，也就是下一层满足了结束条件，然后注意修改一下输入的条件，把问题拆成小问题就是。
#然后就是函数的主体功能，它的功能就是利用下一层的返回值解决当前的问题，然后把结果返回给上一层

#动态规划
def dp_MC(L:list,change):
    best_num2 = {}
    best_num2[0] = 0
    for i in range(1,change+1):
        best_num2[i] = float('inf')
        for c in L:
            if c <= i:
                best_num2[i] = min(best_num2[i],best_num2[i-c] + 1)
    return best_num2[change] if best_num2[change] != float('inf') else -1
L = [1,5,10,21,25]
print(dp_MC(L,63))
# 动态规划的迭代实现与递归算法（自上而下）相反：递归算法是从上往下，逐步拆解问题，一直拆解到最小问题，然后逐步返回，利用返回值解决开始的大问题，而动态规划（迭代版）是从下往上，先给出最小问题的答案，然后一层层往上推导，所以类比于递归算法的结束条件，动态规划一定要先写初始条件，直接确定最小子问题的答案 
# 然后是状态转移过程，同样也是拆解大问题为小问题，和递归“假装小问题解决”不同，这里小问题是真的已经解决（因为从下往上算） 
# 最后是函数的主体功能：我们只需要考虑不同拆解方法对应的结果，选出最符合条件（最优）的那个值。 
# 以上面找零钱为例：它的初始条件就是0元硬币的最优解就是0，转态转移就是把找i元的最少硬币数，拆解成“找i - c元的最优解+1”（c是不同面额），函数的主题功能就是比较不同c对应的（best_nums[i-c]+1）的最小值即可。 
# 这能保证最优解的原因：大问题的最优解一定是若干小问题最优解组成。 
# 反证法验证：如果存在非（best_num2[i-c]+1）的拆解方法找到最优解k（k<所有best_num2[i-c]+1），那么k必然是“选某个面额c + 凑i-c元的硬币数k-1”， # 因为k<所有dp[i-c]+1，所以k-1<dp[i-c]，但dp[i-c]本身是i-c元的最优解，这就矛盾了，因此不存在更优解。