# 补充Vertex类的getWeight方法（获取到邻接顶点的权重）
class Vertex():
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}  # key=邻接顶点，value=边权重
        self.color = 'white'
        self.distance = float('inf')  # 初始化为无穷大（到起点的距离）
        self.pred = None  # 前驱顶点（最短路径的上一个顶点）
        self.discovery_time = 0
        self.finish_time = 0

    def addNeighbor(self, nbr, weight=1):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return list(self.connectedTo.keys())

    def getWeight(self, nbr):  # 新增：获取到邻接顶点的权重
        return self.connectedTo.get(nbr, float('inf'))

    def getId(self):
        return self.id

    # 其他方法（setColor/getColor/setPred/getPred）保持不变
    def setColor(self, color):
        self.color = color
    def getColor(self):
        return self.color
    def setPred(self, vert):
        self.pred = vert
    def getPred(self):
        return self.pred
    def setDistance(self, dist):  # 补充：设置距离
        self.distance = dist
    def getDistance(self):  # 补充：获取距离
        return self.distance

# Graph类完全复用（支持有向边，addEdge是单向）
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

    def addEdge(self, from_key, to_key, weight=1):
        if from_key not in self.vertList:
            self.addVertex(from_key)
        if to_key not in self.vertList:
            self.addVertex(to_key)
        from_vert = self.vertList[from_key]
        to_vert = self.vertList[to_key]
        from_vert.addNeighbor(to_vert, weight)  # 单向边（无向图则双向addEdge）

    def getVertices(self):
        return list(self.vertList.keys())
import heapq

def dijkstra(graph: Graph, start_key):
    """
    Dijkstra算法：单源最短路径
    :param graph: 带权非负图（边权重≥0）
    :param start_key: 起点顶点ID
    :return: 字典（顶点ID: 到起点的最短距离）、字典（顶点ID: 前驱顶点ID）
    """
    # 1. 初始化
    start_vert = graph.getVertex(start_key)
    if not start_vert:
        raise ValueError("起点顶点不存在！")
    
    # 所有顶点距离初始化为无穷大，起点距离设为0
    for vert_id in graph.getVertices():
        vert = graph.getVertex(vert_id)
        vert.setDistance(float('inf'))
        vert.setPred(None)
    start_vert.setDistance(0)

    # 优先队列（最小堆）：存储 (当前距离, 顶点ID)，初始加入起点
    priority_queue = []
    heapq.heappush(priority_queue, (0, start_key))

    # 2. 核心循环：贪心选择+松弛操作
    while priority_queue:
        # 取出距离起点最近的顶点
        current_dist, current_id = heapq.heappop(priority_queue)
        current_vert = graph.getVertex(current_id)

        # 如果当前距离大于已记录的最短距离，跳过（堆中可能有旧的无效数据）
        if current_dist > current_vert.getDistance():
            continue

        # 标记为已访问
        current_vert.setColor('black')

        # 松弛操作：遍历所有邻接顶点
        for neighbor in current_vert.getConnections():
            # 跳过已访问的邻接顶点
            if neighbor.getColor() == 'black':
                continue
            
            # 计算经过当前顶点到邻接顶点的距离
            new_dist = current_vert.getDistance() + current_vert.getWeight(neighbor)
            
            # 如果新距离更短，更新
            if new_dist < neighbor.getDistance():
                neighbor.setDistance(new_dist)
                neighbor.setPred(current_vert)  # 记录前驱顶点
                # 加入优先队列（堆允许重复，后续会跳过无效数据）
                heapq.heappush(priority_queue, (new_dist, neighbor.getId()))

    # 3. 整理结果：距离字典 + 前驱字典
    dist_dict = {vert_id: graph.getVertex(vert_id).getDistance() for vert_id in graph.getVertices()}
    pred_dict = {}
    for vert_id in graph.getVertices():
        pred_vert = graph.getVertex(vert_id).getPred()
        pred_dict[vert_id] = pred_vert.getId() if pred_vert else None

    return dist_dict, pred_dict
#====================测试代码=====================
# 测试函数
def test_dijkstra():
    # 1. 构建带权有向图
    weighted_graph = Graph()
    # 添加边：from_key, to_key, weight
    weighted_graph.addEdge(0, 1, 2)
    weighted_graph.addEdge(0, 2, 5)
    weighted_graph.addEdge(1, 2, 1)
    weighted_graph.addEdge(1, 3, 7)
    weighted_graph.addEdge(2, 3, 1)
    weighted_graph.addEdge(2, 4, 3)
    weighted_graph.addEdge(3, 4, 1)

    # 2. 执行Dijkstra算法（起点为0）
    dist_dict, pred_dict = dijkstra(weighted_graph, start_key=0)

    # 3. 输出结果
    print("=== Dijkstra算法结果（起点0）===")
    print("顶点ID → 到起点的最短距离：")
    for vert_id in sorted(dist_dict.keys()):
        print(f"顶点{vert_id}: {dist_dict[vert_id]}")
    
    print("\n顶点ID → 最短路径前驱顶点：")
    for vert_id in sorted(pred_dict.keys()):
        print(f"顶点{vert_id}: {pred_dict[vert_id]}")

# 运行测试
if __name__ == "__main__":
    test_dijkstra()