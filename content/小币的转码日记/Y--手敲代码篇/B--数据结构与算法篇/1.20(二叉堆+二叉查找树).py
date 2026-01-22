#二叉堆，符合完全二叉树和堆次序的数据结构，完全二叉树是指，叶节点只出现在最底层或者次底层，且叶节点都连续排列在左边，这样的好处减少计算，如果父节点的次序是p，其左节点就是2p，右节点就是2p+1，它的父节点就是p//2，降低复杂度（前提是根为1，如果根为0的话有个偏移值1）。堆次序是指父节点的key比所有子节点都大或者都小
class BinHeap():
    def __init__(self,alist = None):
        if alist is None:
            self.heaplist = []
        else:
             self.heaplist = alist.copy()
#实现insert功能主要两步，先把它塞到最底部，也就是最左的位置，然后上浮，与它的父节点进行比较，然后小于父节点，就交换二者的位置
    def insert(self,newvalue):
        '''
        Docstring for insert
        这里说是二叉树的结构，但是并不是不是物理储存为显性二叉树，而是逻辑结构的隐形二叉树，也就是说这里保存数据时使用list储存的，list是天生的完成二叉树，但是后续操作比如加入，删除，等都是二叉堆的逻辑
        '''
        self.heaplist.append(newvalue)
        current_index = len(self.heaplist) - 1
        while current_index > 0:
            parent_index = (current_index - 1) // 2
            if self.heaplist[current_index] < self.heaplist[parent_index]:
                self.heaplist[current_index],self.heaplist[parent_index]=self.heaplist[parent_index],self.heaplist[current_index]
                current_index = parent_index
            else:
                break
        return 
    def delmin(self):
        '''
        Docstring for delmin
        这里删除最小值自然是删除根节点喽，然后为了保证二叉堆的性质，我们选择的是选取最后一个节点，先让它作为根节点，然后在下沉到合适的位置
        '''
        if len(self.heaplist) == 0:
             return None
        Bottom_num = self.heaplist[-1]
        retval = self.heaplist[0]
        self.heaplist[0] = Bottom_num
        self.heaplist.pop()
        current_index = 0
        while True:
            left = 2*current_index + 1
            right = 2*current_index + 2
            child_index = None
            if left < len(self.heaplist):
                 child_index = left
            if right < len(self.heaplist) and self.heaplist[left] > self.heaplist[right]:
                child_index = right
            if child_index is None or self.heaplist[current_index] <= self.heaplist[child_index]:
                break
            self.heaplist[current_index],self.heaplist[child_index] = self.heaplist[child_index],self.heaplist[current_index]
            current_index = child_index
        return retval
def builtheap(alist):
        '''
        Docstring for builtheap
        input:无序数组
        output:符合二叉堆性质的数组，这一版我是使用了先创建一个空数组，然后对原数组的每一个元素都插入进去，复杂度是nlogn
        '''
        Bh = BinHeap()
        for i in alist:
             Bh.insert(i)
        return Bh.heaplist

def builtheap(alist):
        '''
        Docstring for builtheap
        input:无序数组
        output:符合二叉堆性质的数组，这一版我是直接在原数组的副本上调整，复杂度是n，逻辑是下往上，对每一个非叶子节点一次下沉调整
        '''
        bh = BinHeap(alist)
        index = len(bh.heaplist) // 2 - 1
        for i in range(index,-1,-1):
             current_index = i
             while True:
                left = 2*current_index + 1
                right = 2*current_index + 2
                child_index = None
                if left < len(bh.heaplist):
                    child_index = left
                if right < len(bh.heaplist) and bh.heaplist[left] > bh.heaplist[right]:
                    child_index = right
                if child_index is None or bh.heaplist[current_index] <= bh.heaplist[child_index]:
                    break
                bh.heaplist[current_index],bh.heaplist[child_index] = bh.heaplist[child_index],bh.heaplist[current_index]
                current_index = child_index
        return bh.heaplist
#二叉查找树，另一种结构，左子树中所有节点的key都小于父节点，右子树中所有节点的key都大于父节点，但是并不需要保证完全二叉树的结构，而且与二叉堆的不同是，它是储存在树结构中的，而不是列表.而且它的特点是在插入新节点时，永远不会移动原有的结构，但是还是能保证，左子树节点能够小于根节点，右子树大于根节点
class TreeNode():
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
class BinarySearchTree():
    def __init__(self):
        self.root = None
        self.size = 0
    def put(self,key,val):
        new_node = TreeNode(key,val)
        if self.root is None:
            self.root = new_node
            self.size += 1
        else:
            current = self.root
            while True:
                if current.key == new_node.key:
                    current.val = new_node.val
                    break
                if current.key > new_node.key:
                    if current.left is None:
                        new_node.parent =  current
                        current.left = new_node
                        self.size += 1
                        break
                    else:
                        current = current.left
                if current.key < new_node.key:
                    if current.right is None:
                        new_node.parent = current
                        current.right = new_node
                        self.size += 1
                        break
                    else:
                        current = current.right
            return
    def get(self,key):
        if self.root == None:
            return None
        current = self.root
        while current:
            if current.key == key:
                return current.val
            if current.key < key:
                current = current.right
            else:
                current = current.left
        return None
    def delete(self,key):
        def get_node(key):
            if self.root == None:
                return None
            current = self.root
            while current:
                if current.key == key:
                    return current
                if current.key < key:
                    current = current.right
                else:
                    current = current.left
            return None
        del_node = get_node(key)
        if not del_node:
            return 
        if not del_node.left and not del_node.right:
            parent = del_node.parent
            if not parent:
                self.root = None
            elif parent.left is del_node:
                parent.left = None
            elif parent.right is del_node:
                parent.right = None
            self.size -= 1
        elif del_node.left and not del_node.right:
            if self.root is del_node:
                self.root = del_node.right
            else:
                parent = del_node.parent
                child = del_node.left
                child.parent = parent
                parent.left = child
            self.size -= 1
        elif not del_node.left and del_node.right:
            if self.root is del_node:
                self.root = del_node.right
            else:
                parent = del_node.parent
                child = del_node.right
                child.parent = parent
                parent.right = child
            self.size -= 1
        else:
            del_node.left and del_node.right
            #这里有两个方法，我们要找一个节点来替代这个节点的位置，一种是找一个刚好比他大一点的节点，那就往它的右子树找，且往右子树的左边找到叶节点，这个值就是右子树的最小值，但是右子树又有大于根节点的特点，所以刚好。也可以往左子树中往右找，找到最大值，刚好也合适
            #这里选择找右子树的最小节点
            current = del_node.right
            while current.left:
                current = current.left
            successor = current
            del_node.key = successor.key
            del_node.val = successor.val
            parent = successor.parent
            parent.left = None
            self.size -= 1
    def inOrder(self):
        if not self.root:
            return []
        res = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(self.root)
        return res
    def preOrder(self):
        if not self.root:
            return []
        res = []
        def preorder(node):
            if not node:
                return
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(self.root)
        return res
    def rearOrder(self):
        if not self.root:
            return []
        res = []
        def rearorder(node):
            if not node:
                return 
            rearorder(node.left)
            rearorder(node.right)
            res.append(node.val)
        rearorder(self.root)
        return res
    def find_max(self):
        if self.size == 0:
            return None
        max_node = self.root
        while max_node.right:
            max_node = max_node.right
        return max_node.key
    def find_min(self):
        if self.size == 0:
            return None
        min_node = self.root
        while min_node.left:
            min_node = min_node.left
        return min_node.key
    def getHeight(self):
        def get_hight(node):
            if not node:
                return -1
            left_hight = get_hight(node.left)
            right_hight = get_hight(node.right)
            return 1 + max(left_hight,right_hight)
        return get_hight(self.root)
    def is_valid_bst_recursive(self):
        """方法1：递归上下界校验（最严谨）"""
        def _valid(node, min_bound, max_bound):
            # 空节点合法
            if not node:
                return True
            # 当前节点key超出上下界 → 不合法
            if node.key <= min_bound or node.key >= max_bound:
                return False
            # 递归校验左子树（左子树max=当前key）、右子树（右子树min=当前key）
            return _valid(node.left, min_bound, node.key) and _valid(node.right, node.key, max_bound)
        
        # 空树视为合法，根节点无上下界限制
        return _valid(self.root, float('-inf'), float('inf'))
    def is_valid_bst_inorder(self):
        """方法2：中序遍历校验（直观易理解）"""
        # 先获取key的中序序列（注意：之前的inOrder返回val，这里要返回key）
        def _inorder_key(node, res):
            if not node:
                return
            _inorder_key(node.left, res)
            res.append(node.key)
            _inorder_key(node.right, res)
        
        key_list = []
        _inorder_key(self.root, key_list)
        
        # 检查序列是否严格升序
        for i in range(1, len(key_list)):
            if key_list[i] <= key_list[i-1]:
                return False
        return True