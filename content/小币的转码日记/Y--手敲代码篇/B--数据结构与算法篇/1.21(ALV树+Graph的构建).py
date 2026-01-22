#AVL树
class AVLNode():
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None
        self.height = 1
class AVLTree():
    def __init__(self):
        self.root = None
    def get_height(self,node:AVLNode):
        if not node:
            return 0
        else:
            return node.height
    def get_balance_factor(self,node:AVLNode):
        leftHeight = self.get_height(node.left)
        rightHeight = self.get_height(node.right)
        return leftHeight - rightHeight
    def right_rotate(self,unbalanced_node):
        '''
        当某个节点的平衡因子大于1时，也就是说左边的高度比右边的高度的高度差大于1，并且这个节点的左子树的平衡因子大于0，就调用该函数
        这里使这个节点重新平衡的逻辑是把过高的左子树的根提拔为新的根，原根降级为右子节点，并且保持整颗树左小右大的性质
        '''
        new_root = unbalanced_node.left
        temp = new_root.right
        new_root.right = unbalanced_node
        unbalanced_node.left = temp
        unbalanced_node.height = 1 + max(self.get_height(unbalanced_node.left),self.get_height(unbalanced_node.right))
        new_root.height = 1 + max(self.get_height(new_root.left),self.get_height(new_root.right))
        return new_root
    def left_rotate(self,unbalanced_node):
        '''
        和上面一样，当该节点的平衡因子小于负一，并且该节点的右子树的平衡因子小于等于0时调用该函数
        它是讲过高的右子树的根提拔为新的根，原根降级为左子节点，同样能保证左小右大的特性
        '''
        new_root = unbalanced_node.right
        temp = new_root.left
        new_root.left = unbalanced_node
        unbalanced_node.right = temp
        unbalanced_node.height = 1 + max(self.get_height(unbalanced_node.left),self.get_height(unbalanced_node.right))
        new_root.height = 1 + max(self.get_height(new_root.left),self.get_height(new_root.right))
        return new_root
    def lr_rotate(self,unbalanced_node):
        '''
        当该节点的平衡因子大于1，并且左节点的平衡因子小于0
        它的逻辑是先左旋左节点，将其左节点的平衡因子大于0，然后再对根节点指向右旋，因为这个时候就符合右旋的条件了
        '''
        new_left = self.left_rotate(unbalanced_node.left)
        unbalanced_node.left = new_left
        new_root = self.right_rotate(unbalanced_node)
        return new_root
    def rl_rotate(self,unbalanced_node):
        '''
        当该节点的平衡因子小于-1，并且右节点的平衡因子大于0
        它的逻辑同样是先右旋右节点，将其右节点的平衡因子小于0，然后对根节点左旋就行
        '''
        new_right = self.right_rotate(unbalanced_node.right)
        unbalanced_node.right = new_right
        new_root = self.left_rotate(unbalanced_node)
        return new_root
    def insert(self,value):
        '''
        简单来说就是先像普通BST一样递归找到位置插入新节点，然后从插入的叶子往上回头，每走一步都更新当前节点的高度，计算平衡因子，如果失衡，就看是哪种失衡，然后给他矫正，并返回上层，让上层更新指针，直到回到根节点，整棵树就平衡了
        '''
        self.root = self._insert_recursive(self.root,value)
    def _insert_recursive(self,current_node,value):
        if not current_node:
            return AVLNode(value)
        if value < current_node.val:
            current_node.left = self._insert_recursive(current_node.left,value)
        elif value > current_node.val:
            current_node.right = self._insert_recursive(current_node.right,value)
        else:
            return current_node
        current_node.height = 1 + max(self.get_height(current_node.left),self.get_height(current_node.right))
        bf = self.get_balance_factor(current_node)
        if bf > 1 and value < current_node.left.val:
            return self.right_rotate(current_node)
        if bf > 1 and value > current_node.left.val:
            return self.lr_rotate(current_node)
        if bf < -1 and value > current_node.right.val:
            return self.left_rotate(current_node)
        if bf < -1 and value < current_node.right.val:
            return self.rl_rotate(current_node)
        return current_node
# ===================== 仅基于你代码的测试代码 =====================
if __name__ == "__main__":
    # 测试1：LL型失衡（插入3→2→1）
    print("===== 测试1：LL型失衡（插入3→2→1） =====")
    avl_ll = AVLTree()
    for val in [3,2,1]:
        avl_ll.insert(val)
    # 验证核心指标（只用你代码里的方法/属性）
    print(f"根节点值（预期2）：{avl_ll.root.val}")
    print(f"根节点平衡因子（预期0）：{avl_ll.get_balance_factor(avl_ll.root)}")
    print(f"根节点高度（预期2）：{avl_ll.get_height(avl_ll.root)}")
    print(f"根左子节点值（预期1）：{avl_ll.root.left.val if avl_ll.root.left else '无'}")
    print(f"根右子节点值（预期3）：{avl_ll.root.right.val if avl_ll.root.right else '无'}")
    print("\n" + "-"*60 + "\n")

    # 测试2：RR型失衡（插入1→2→3）
    print("===== 测试2：RR型失衡（插入1→2→3） =====")
    avl_rr = AVLTree()
    for val in [1,2,3]:
        avl_rr.insert(val)
    print(f"根节点值（预期2）：{avl_rr.root.val}")
    print(f"根节点平衡因子（预期0）：{avl_rr.get_balance_factor(avl_rr.root)}")
    print(f"根节点高度（预期2）：{avl_rr.get_height(avl_rr.root)}")
    print(f"根左子节点值（预期1）：{avl_rr.root.left.val if avl_rr.root.left else '无'}")
    print(f"根右子节点值（预期3）：{avl_rr.root.right.val if avl_rr.root.right else '无'}")
    print("\n" + "-"*60 + "\n")

    # 测试3：LR型失衡（插入3→1→2）
    print("===== 测试3：LR型失衡（插入3→1→2） =====")
    avl_lr = AVLTree()
    for val in [3,1,2]:
        avl_lr.insert(val)
    print(f"根节点值（预期2）：{avl_lr.root.val}")
    print(f"根节点平衡因子（预期0）：{avl_lr.get_balance_factor(avl_lr.root)}")
    print(f"根节点高度（预期2）：{avl_lr.get_height(avl_lr.root)}")
    print(f"根左子节点值（预期1）：{avl_lr.root.left.val if avl_lr.root.left else '无'}")
    print(f"根右子节点值（预期3）：{avl_lr.root.right.val if avl_lr.root.right else '无'}")
    print("\n" + "-"*60 + "\n")

    # 测试4：RL型失衡（插入1→3→2）
    print("===== 测试4：RL型失衡（插入1→3→2） =====")
    avl_rl = AVLTree()
    for val in [1,3,2]:
        avl_rl.insert(val)
    print(f"根节点值（预期2）：{avl_rl.root.val}")
    print(f"根节点平衡因子（预期0）：{avl_rl.get_balance_factor(avl_rl.root)}")
    print(f"根节点高度（预期2）：{avl_rl.get_height(avl_rl.root)}")
    print(f"根左子节点值（预期1）：{avl_rl.root.left.val if avl_rl.root.left else '无'}")
    print(f"根右子节点值（预期3）：{avl_rl.root.right.val if avl_rl.root.right else '无'}")
    print("\n" + "-"*60 + "\n")

    # 测试5：重复值插入（不插入）
    print("===== 测试5：重复值插入 =====")
    avl_dup = AVLTree()
    avl_dup.insert(5)
    avl_dup.insert(5)
    print(f"根节点值（预期5）：{avl_dup.root.val}")
    print(f"根节点左/右子节点（预期无）：{avl_dup.root.left} / {avl_dup.root.right}")
#Graph的构建
class Vertex():
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
    def addNeighbor(self,nbr:Vertex,weight = 0):
        self.connectedTo[nbr] = weight
    def getConnections(self):
        return list(self.connectedTo.keys())
    def getId(self):
        return self.id
    def getWeight(self,nbr):
        return self.connectedTo.get(nbr)
class Graph():
    def __init__(self):
        self.vertlist = {}#key是顶点的id，value是对应的Vertex对象
        self.numVertices = 0
    def addVertex(self,key):
        new_vertex = Vertex(key)
        self.vertlist[key] = new_vertex
        self.numVertices += 1
        return new_vertex
    def getVertex(self,key):
        return self.vertlist.get(key)
    def addEdge(self,start_key,end_key,weight = 0):
        if self.getVertex(start_key) is None:
            self.addVertex(start_key)
        if self.getVertex(end_key) is None:
            self.addVertex(end_key)
        start_vert = self.getVertex(start_key)
        end_vert = self.getVertex(end_key)
        start_vert.addNeighbor(end_vert,weight)
    def getVertices(self):
        return list(self.vertlist.keys())
    def __iter__(self):
        '''这个__iter__的功能是python内部的迭代器方法，有了这个功能后，就能遍历graph中的Vertex对象（因为我后面写的九四vertex对象，也因为通常遍历的就是vertex对象）'''
        return iter(self.vertlist.values())
    def __str__(self):
        res = []
        for vert in self:
            vert_id = vert.getId()
            neighbors = []
            for nbr in vert.getConnections():
                nbr_id = nbr.getId()
                weight = vert.getWeight(nbr)
                neighbors.append(f"顶点{nbr_id}(权重{weight})")
            res.append(f"顶点{vert_id}的邻接顶点：{','.join(neighbors) if neighbors else '无'}")
        return "\n".join(res)
# ===================== 测试代码 =====================
if __name__ == "__main__":
    # 1. 创建空图
    print("===== 1. 创建空图 =====")
    g = Graph()

    # 2. 测试添加边（自动创建顶点）：添加有向边 0→1（无权，默认权重0）、0→2（有权，权重5）、1→3（权重3）
    print("\n===== 2. 添加边（自动创建顶点） =====")
    g.addEdge(0, 1)       # 无权边：0→1
    g.addEdge(0, 2, 5)    # 有权边：0→2（权重5）
    g.addEdge(1, 3, 3)    # 有权边：1→3（权重3）

    # 3. 测试获取所有顶点id
    print("\n===== 3. 获取所有顶点id =====")
    vertices = g.getVertices()
    print(f"图中所有顶点id：{vertices}")  # 预期：[0,1,2,3]

    # 4. 测试遍历顶点对象（利用__iter__方法）
    print("\n===== 4. 遍历所有顶点对象 =====")
    for vert in g:
        print(f"当前顶点id：{vert.getId()}")

    # 5. 测试打印图的完整结构（利用__str__方法）
    print("\n===== 5. 打印图的完整结构 =====")
    print(g)

    # 6. 测试获取指定顶点的邻接关系和边权重
    print("\n===== 6. 获取指定顶点的邻接信息 =====")
    v0 = g.getVertex(0)
    print(f"顶点0的邻接顶点对象列表：{[nbr.getId() for nbr in v0.getConnections()]}")  # 预期：[1,2]
    print(f"顶点0到顶点1的边权重：{v0.getWeight(g.getVertex(1))}")  # 预期：0
    print(f"顶点0到顶点2的边权重：{v0.getWeight(g.getVertex(2))}")  # 预期：5

    # 7. 测试获取不存在的顶点/权重
    print("\n===== 7. 测试边界情况（获取不存在的顶点/权重） =====")
    v5 = g.getVertex(5)
    print(f"获取不存在的顶点5：{v5}")  # 预期：None
    print(f"顶点1到顶点5的边权重：{g.getVertex(1).getWeight(g.getVertex(5))}")  # 预期：None
