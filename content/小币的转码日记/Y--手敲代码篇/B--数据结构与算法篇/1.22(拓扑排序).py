class Vertex():
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}  # 邻接顶点（有向边：key=邻接顶点，value=权重）
        self.color = 'white'   # 遍历状态：white=未访问，gray=访问中，black=已访问
        self.distance = -1
        self.pred = None
        # 新增：DFS时间戳（拓扑排序需要）
        self.discovery_time = 0  # 首次访问时间
        self.finish_time = 0     # 遍历完所有邻接顶点的时间

    def addNeighbor(self, nbr, weight=1):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return list(self.connectedTo.keys())

    def getId(self):  # 新增：方便获取顶点ID
        return self.id

    # 其他方法（setColor/getColor等）保持不变
    def setColor(self, color):
        self.color = color
    def getColor(self):
        return self.color
    def setPred(self, vert):
        self.pred = vert
    def getPred(self):
        return self.pred

class Graph():
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        if key not in self.vertList:
            self.numVertices += 1
            new_vert = Vertex(key)
            self.vertList[key] = new_vert
        return self.vertList[key]

    def getVertex(self, key):
        return self.vertList.get(key)

    # 关键调整：有向边（仅添加 fromvert → tovert，不反向）
    def addEdge(self, from_key, to_key, weight=1):
        if from_key not in self.vertList:
            self.addVertex(from_key)
        if to_key not in self.vertList:
            self.addVertex(to_key)
        from_vert = self.vertList[from_key]
        to_vert = self.vertList[to_key]
        from_vert.addNeighbor(to_vert, weight)  # 仅单向添加

    def getVertices(self):
        return list(self.vertList.keys())
# 全局时间戳（DFS遍历用）
time = 0

def topological_sort_dfs(graph: Graph):
    """
    基于DFS的拓扑排序
    :param graph: 有向无环图（DAG）
    :return: 拓扑排序结果列表（顶点ID）
    """
    global time
    time = 0  # 初始化时间戳
    topo_order = []  # 存储后序遍历结果（最终逆序为拓扑排序）

    # 嵌套：核心DFS函数
    def dfs(vert: Vertex):
        global time
        vert.setColor('gray')  # 标记为“访问中”
        time += 1
        vert.discovery_time = time  # 记录发现时间

        # 遍历所有邻接顶点
        for neighbor in vert.getConnections():
            if neighbor.getColor() == 'white':
                neighbor.setPred(vert)
                dfs(neighbor)  # 递归遍历邻接顶点

        # 后序：遍历完所有邻接顶点后，加入结果
        vert.setColor('black')
        time += 1
        vert.finish_time = time
        topo_order.append(vert.getId())  # 后序添加

    # 遍历所有未访问的顶点（处理非连通DAG）
    for vert_id in graph.getVertices():
        vert = graph.getVertex(vert_id)
        if vert.getColor() == 'white':
            dfs(vert)

    # 逆序后序结果 = 拓扑排序
    return topo_order[::-1]
#===================测试代码===================
# 测试函数
def test_topological_sort():
    # 1. 构建有向无环图（课程依赖）
    course_graph = Graph()
    # 添加有向边：from 依赖课程 → to 被依赖课程
    course_graph.addEdge(1, 0)   # 选0前必须选1
    course_graph.addEdge(2, 1)   # 选1前必须选2
    course_graph.addEdge(1, 3)   # 选3前必须选1
    course_graph.addEdge(3, 4)   # 选4前必须选3

    # 2. 执行拓扑排序
    topo_result = topological_sort_dfs(course_graph)
    print("拓扑排序结果（课程选择顺序）：", topo_result)

# 运行测试
if __name__ == "__main__":
    test_topological_sort()