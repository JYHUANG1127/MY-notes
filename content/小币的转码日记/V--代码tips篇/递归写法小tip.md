```python
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

#然后是什么时候要调用自身，也就是非问题最小值的情况，应该怎么拆分问题，记住这个时候需要假装下一层的函数工作已经完成了，也就是下一层满足了结束条件，然后注意修改一下输入的条件，把问题拆成小问题就是。

#然后就是函数的主体功能，它的功能就是利用下一层的返回值解决当前的问题，然后把结果返回给上一层，记住我们假装拿到的返回值要与我们这一层返回给上一层的返回值是一个东西，也就是主体函数等待输入的部分与输出部分要是同一类东西
```