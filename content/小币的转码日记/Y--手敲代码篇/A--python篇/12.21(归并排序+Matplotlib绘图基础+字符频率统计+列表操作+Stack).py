import time
def merge(left,right):
    result = []
    i = j =0 # i and j are indexes for left and right lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):#append remaining elements
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result
def merge_sort(L):
    t0 =time.perf_counter()
    if len(L) < 2:
        print("Time taken for sorting a list of length",len(L),"is",time.perf_counter() - t0)
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        print("Time taken for sorting a list of length",len(L),"is",time.perf_counter() - t0)
        return merge(left,right)
# merge_sort的核心思想是将一个列表分为左右两部分，分别对这两个部分进行排序，排序的方法利用递归的思想，将左右两个部分再分为两部分，直到左右分别为1，或者0个元素。然后开始融合左右两个部分的元素，比较两个部分的第一个元素，然后将其加入到result中，然后比较下一个。如果比较结束之后还有没进行比较的就直接加入到result中
L=[23,423,534,534,5,446,5,7,68,7,8345,5,334,766787,978954,6,436,46,53345,76,3]
print(merge_sort(L))

from matplotlib import pyplot as plt
plt.figure('random')
plt.plot([1,3,5,7,9],[2,4,6,8,10],label='random',marker='*',color='b',linestyle='--')
plt.title('random plot')
plt.xlabel('random x axis')
plt.ylabel('random y axis')
plt.xlim(1,10)
plt.ylim(2,12)
plt.xticks([1,2,3,4,5,6,7,8,9,10])
plt.grid()
plt.figure('random second')
plt.scatter([213,32,4,5,6,735,322,4,342,654],[213,543,543,6,7,887,32,43,65,76],label='random second',marker='o',color='r')
plt.show()

#下面是计算每个字母出现次数的代码，用来判断字母异位词很方便，重要的是复杂度很低
def letter_counter(s):
    count = {}
    for letter in s:
        pos = ord(letter)-ord('a')
        count[pos] =count[pos]+1 if pos in count else 1
    return count
s1 = 'saiuvbfyuavruyesver'
s2 = 'daddfsdafafe'
def letter_countersecond(s):
    count=[0]*26
    for letter in s:
        pos = ord(letter)-ord('a')
        count[pos] += 1 if pos in count else 1
    return count
print(letter_countersecond(s1))
print(letter_countersecond(s2))

L1=[12345,678,32]
L1.extend([3123,43,534])
print(L1)
L1.insert(2,[123,456])
print(L1)
L1.insert(1,144)
print(L1)
a=L1.pop(2)
print(a)
print(L1.index(43))
print(L1.count(678))

class Stack(object):
    def __init__ (self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
#下面是利用栈来将十进制转化为二进制
def devide_by_2(dec_number):
    rem_stack = Stack()
    while dec_number > 0:
        rem =dec_number%2
        rem_stack.push(rem)
        dec_number = dec_number // 2
    bin_string = ''
    while not rem_stack.is_empty():
        bin_string = bin_string +str(rem_stack.pop())
    return bin_string
print(devide_by_2(10086))

#下面是利用栈来将一个中缀表达式转化为后缀表达式
class Stack(object):
    def __init__ (self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
def infix_to_postfix(infix_expr):
    opstack = Stack()
    postlist = []
    prec={}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    prec[")"] = 1
    token_list = infix_expr.split(' ')
    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postlist.append(token)
        elif token == "(":
            opstack.push(token)
        elif token == ")":
            while not opstack.is_empty():
                top_token = opstack.pop()
                if top_token =="(":
                    break
                else:
                    postlist.append(top_token)
        elif token in "+-*/":
            while (not opstack.is_empty()) and (prec[opstack.peek()] > prec[token]):
                postlist.append(opstack.pop())
            opstack.push(token)
    while not opstack.is_empty():
        postlist.append(opstack.pop())
    return ' '.join(postlist)
print(infix_to_postfix("A + B * C - ( D / E + F ) * G"))
#下面是利用栈来计算一个后缀表达式的值
class Stack(object):
    def __init__ (self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
def domath(op,op1,op2):
    if op == "+":
        return op2 + op1
    elif op == "-":
        return op2 - op2
    elif op == "*":
        return op2 * op1
    elif op == "/":
        return op2 / op1
def postfix_eval(postfix_expr):
    operand_stack = Stack()
    token_list = postfix_expr.split()
    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        elif token in "+-*/":
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = domath(token,operand1,operand2)
            operand_stack.push(result)
    return operand_stack.pop()
print(postfix_eval("7 8 + 3 2 + /"))