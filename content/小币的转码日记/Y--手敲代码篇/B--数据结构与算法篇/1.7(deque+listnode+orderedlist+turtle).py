class deque:
    def __init__(self):
        self.items = []
    def addFront(self,item):
        self.items.insert(0,item)
    def addRear(self,item):
        self.items.append(item)
    def removeFront(self):
        return self.items.pop(0)
    def removeRear(self):
        return self.items.pop()
    def getSize(self):
        return len(self.items)
def palchecker(str):
    str_charact = deque()
    if_pal = True
    for i in str:
        str_charact.addFront(i)
    n = str_charact.getSize()
    for i in range(n//2):
        x = str_charact.removeFront()
        y = str_charact.removeRear()
        if x != y:
            if_pal = False
            break
    return if_pal
print(palchecker(''))
print(palchecker('a'))
print(palchecker('radar'))
print(palchecker('level'))
print(palchecker('abba'))
print(palchecker('hello'))
print(palchecker('python'))
print(palchecker('student'))

class listnode:
    def __init__(self,value = 0,next = None):
        self.val = value
        self.next = next
def isEmpty(head):
    return head == None
def add(head,item:listnode):
    item.next = head
    return item
def size(head:listnode):
    x = 0
    while head:
        x += 1
        head = head.next
    return x
def search(head:listnode,item):
    if_exit = False
    while head:
        if head.val == item:
            if_exit = True
            break
        head = head.next
    return if_exit
def remove(head:listnode,item):
    dummy = listnode(0)
    dummy.next = head
    pre = dummy
    cur = head
    while cur:
        if cur.val == item:
            nextnode = cur.next
            pre.next = nextnode
            break
        pre = pre.next
        cur = cur.next
    return dummy.next
# 仅测试逻辑代码（需确保已定义 listnode 类和对应链表操作函数）
# 场景1：空链表基础操作
print("===== 测试场景1：空链表基础操作 =====")
head = None
print(f"空链表是否为空: {isEmpty(head)} (预期: True)")
print(f"空链表长度: {size(head)} (预期: 0)")
print(f"空链表搜索10: {search(head, 10)} (预期: False)")
new_head = remove(head, 10)
print(f"空链表删除10后head是否为None: {new_head is None} (预期: True)\n")

# 场景2：插入单个节点
print("===== 测试场景2：插入单个节点 =====")
node1 = listnode(10)
head = add(None, node1)
print(f"单节点链表头值: {head.val} (预期: 10)")
print(f"单节点链表是否为空: {isEmpty(head)} (预期: False)")
print(f"单节点链表长度: {size(head)} (预期: 1)")
print(f"搜索存在值10: {search(head, 10)} (预期: True)")
print(f"搜索不存在值20: {search(head, 20)} (预期: False)\n")

# 场景3：插入多个节点（头插法）
print("===== 测试场景3：插入多个节点 =====")
head = None
node1 = listnode(10)
node2 = listnode(20)
node3 = listnode(30)
head = add(None, node1)
head = add(head, node2)
head = add(head, node3)
print(f"多节点链表头值: {head.val} (预期: 30)")
print(f"第二个节点值: {head.next.val} (预期: 20)")
print(f"第三个节点值: {head.next.next.val} (预期: 10)")
print(f"多节点链表长度: {size(head)} (预期: 3)")
print(f"搜索中间值20: {search(head, 20)} (预期: True)\n")

# 场景4：删除头节点
print("===== 测试场景4：删除头节点 =====")
head = remove(head, 30)
print(f"删除头节点后新头值: {head.val} (预期: 20)")
print(f"删除后长度: {size(head)} (预期: 2)\n")

# 场景5：删除中间节点
print("===== 测试场景5：删除中间节点 =====")
head = None
node1 = listnode(5)
node2 = listnode(10)
node3 = listnode(20)
head = add(None, node1)
head = add(head, node2)
head = add(head, node3)
head = remove(head, 10)
print(f"删除中间节点后长度: {size(head)} (预期: 2)")
print(f"搜索10是否存在: {search(head, 10)} (预期: False)")
print(f"删除后节点顺序: {head.val} → {head.next.val} (预期: 20 → 5)\n")

# 场景6：删除仅有的一个节点
print("===== 测试场景6：删除单节点 =====")
head = None
node = listnode(8)
head = add(None, node)
head = remove(head, 8)
print(f"删除单节点后head是否为None: {head is None} (预期: True)")
print(f"删除后是否为空: {isEmpty(head)} (预期: True)")
print(f"删除后长度: {size(head)} (预期: 0)\n")

# 场景7：删除不存在的节点
print("===== 测试场景7：删除不存在的节点 =====")
head = None
node1 = listnode(20)
node2 = listnode(10)
head = add(None, node1)
head = add(head, node2)
original_size = size(head)
head = remove(head, 30)
print(f"删除不存在节点后长度: {size(head)} (预期: {original_size})")
print(f"删除后节点顺序: {head.val} → {head.next.val} (预期: 10 → 20)")

class orderedlist:
    def __init__(self):
        self.items = []
    def add(self,item):
        lenth = len(self.items)
        if lenth == 0 or self.items[lenth-1] < item:
            self.items.append(item)
            return self.items
        for i in range(lenth):
            if self.items[i] > item:
                self.items.insert(i,item)
                break
        return self.items
    def remove(self,item):
        self.items.remove(item)
        return self.items
    def search(self,item):
        if_exit = False
        for i in self.items:
            if i == item:
                if_exit = True
        return if_exit
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def index(self,item):
        Index = None
        n = len(self.items)
        for i in range(n):
            if self.items[i] == item:
                Index = i
        return Index +1 if Index else Index
    def pop(self,pos = -1):
        return self.items.pop(pos)
#创建海龟对象，将画笔粗细设置为 3 像素
import turtle
t = turtle.Turtle()
t.pensize(3)
#绘制外层正方形：把画笔颜色设为红色；绘制一个边长为 150 像素的正正方形（仅用forward()和right()/left()实现转向）；
t.pencolor("red")
t.forward(150)
t.right(90)
t.forward(150)
t.right(90)
t.forward(150)
t.right(90)
t.forward(150)
#移动海龟到内层位置：抬起画笔（避免移动时画线），将海龟向右移动 30 像素、再向上移动 30 像素；放下画笔，恢复画线状态；
t.penup()
t.left(90)
t.forward(30)
t.left(90)
t.forward(30)
t.pendown()
#绘制内层正方形：把画笔颜色改为蓝色；绘制一个边长为 90 像素的正正方形；
t.pencolor("blue")
t.forward(90)
t.left(90)
t.forward(90)
t.left(90)
t.forward(90)
t.left(90)
t.forward(90)
turtle.done()