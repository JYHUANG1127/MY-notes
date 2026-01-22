#ADT map类，但是最多只能储存11对key和val，而且当删除一个元素时，另一个因为哈希冲突被挤开的元素，可能会在使用get函数时报错，可以添加一个标记告诉python这个哈希值曾经被删除过，不能提前返回
class Map():
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
    def put(self,key,value):
        index = key % self.size
        if self.slots[index] == None:
            self.slots[index] = key
            self.data[index] = value
        elif self.slots[index] == key:
            self.data[index] = value
        else:
            while self.slots[index] != None:
                index = index +1
                if index == self.size:
                    index = 0
            self.slots[index] = key
            self.data[index] = value
    def get(self,key):
        index = key % self.size
        if self.slots[index] == None:
            return None
        if self.slots[index] == key:
            return self.data[index]
        x = 0
        while self.slots[index] != key and self.slots[index] != None and x <= self.size:
            index = index + 1 
            if index == self.size:
                index = 0
            x += 1
        if x == self.size:
            return None
        else:
            return self.data[index]
    def delitem(self,key):
        index = key % self.size
        if self.slots[index] == None:
            return print('key is not exist')
        if self.slots[index] == key:
            self.slots[index] = None
            self.data[index] = None
            return
        x = 0
        while self.slots[index] != key and self.slots[index] != None and x <= self.size:
            index = index +1
            if index == self.size:
                index = 0
            x += 1
        if x == self.size: 
            return print('key is not exist')
        else:
            self.slots[index] = None
            self.data[index] = None
    def len(self):
        num = 0
        for i in self.slots:
            if i != None:
                num += 1
        return num
    def if_exist(self,key):
        val = self.get(key)
        if val != None:
            return True
        else:
            return False
#用list和递归来构建一个树的类
def binaryTree(r):
    return [r,[],[]]
def insertleft(r,branch):
    t = r.pop(1)
    if len(t) > 1:
        r.insert(1,[branch,t,[]])
    else:
        r.insert(1,[branch,[],[]])
    return r
def insertRight(r,branch):
    t = r.pop(2)
    if len(t) > 1:
        r.insert(2,[branch,[],t])
    else:
        r.insert(2,[branch,[],[]])
    return r
def getRootVal(r):
    return r[0]
def setRootVal(r,val):
    r[0] = val
    return r
def getLeftChild(r):
    return r[1]
def getRightChild(r):
    return r[2]
#用节点链接的方式来实现树，也就是每一个节点都存在key，left，right分别指向左子节点和右子节点
class BinaryTree():
    def __init__(self,val,key = ''):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
    def insertLeft(self,newnode:binaryTree):
        if self.left == None:
            self.left = newnode
        else:
            nextnode = self.left
            self.left = newnode
            newnode.left = nextnode
    def insertRight(self,newnode:binaryTree):
        if self.right == None:
            self.right = newnode
        else:
            nextnode = self.right
            self.right = newnode
            newnode.right = nextnode
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def setRootVal(self,newVal):
        self.val = newVal
    def setRootKey(self,newKey):
        self.key = newKey
    def getRootVal(self):
        return self.val
    def getRootKey(self):
        return self.key
#前序遍历，中序遍历，后续遍历链表二叉树
def preorder(head):
    res = []
    def preOrder(node):
        if not node:
            return 
        res.append(node.val)
        preOrder(node.left)
        preOrder(node.right)
    preOrder(head)
    return res
def inorder(head):
    res = []
    def inOrder(node):
        if not node:
            return 
        inOrder(node.left)
        res.append(node.val)
        inOrder(node.right)
    inOrder(head)
    return res
def rearorder(head):
    res = []
    def rearOrder(node):
        if not node:
            return 
        rearOrder(node.left)
        rearOrder(node.right)
        res.append(node.val)
    rearOrder(head)
    return res
#表达式的拆解，将一个表达式拆解，每个节点或者代表计算量或者代表符号或者代表括号
from collections import deque
def buildParseTree(fpexp):
    '''
    fpexp必须是全括号表达式
    '''
    fplist = fpexp.split()
    pStack = deque()
    eTree = BinaryTree('')
    pStack.append(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.append(currentTree)
            currentTree = currentTree.getLeft()
        elif i not in ['+','-','*','/',')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+','-','*','/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.append(currentTree)
            currentTree = currentTree.getRight()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree
#表达式的合成，把上面拆成的表达式合成，然后就可以计算
import operator
def evaluate(parseTree:BinaryTree):
    opers = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    leftC = parseTree.getLeft()
    rightC = parseTree.getRight()
    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()

