# Vertex类完全复用Dijkstra中的版本（包含distance/pred/getWeight等）
class Vertex():
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.distance = float('inf')  # 到已选集合的最小距离（边权重）
        self.pred = None  # 最小生成树中的前驱顶点
        self.discovery_time = 0
        self.finish_time = 0

    def addNeighbor(self, nbr, weight=1):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return list(self.connectedTo.keys())

    def getWeight(self, nbr):
        return self.connectedTo.get(nbr, float('inf'))

    def getId(self):
        return self.id

    def setColor(self, color):
        self.color = color
    def getColor(self):
        return self.color
    def setPred(self, vert):
        self.pred = vert
    def getPred(self):
        return self.pred
    def setDistance(self, dist):
        self.distance = dist
    def getDistance(self):
        return self.distance

# Graph类调整为无向图（addEdge双向添加）
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

    # 关键调整：无向图→双向添加边
    def addEdge(self, from_key, to_key, weight=1):
        if from_key not in self.vertList:
            self.addVertex(from_key)
        if to_key not in self.vertList:
            self.addVertex(to_key)
        from_vert = self.vertList[from_key]
        to_vert = self.vertList[to_key]
        from_vert.addNeighbor(to_vert, weight)
        to_vert.addNeighbor(from_vert, weight)  # 无向图：双向添加

    def getVertices(self):
        return list(self.vertList.keys())
import heapq

def prim(graph: Graph, start_key):
    """
    Prim算法：最小生成树（MST）
    :param graph: 无向带权连通图
    :param start_key: 起点顶点ID
    :return: 字典（顶点ID: 前驱顶点ID）、最小生成树总权重
    """
    # 1. 初始化
    start_vert = graph.getVertex(start_key)
    if not start_vert:
        raise ValueError("起点顶点不存在！")
    
    # 所有顶点到已选集合的距离初始化为无穷大，起点距离设为0
    for vert_id in graph.getVertices():
        vert = graph.getVertex(vert_id)
        vert.setDistance(float('inf'))
        vert.setPred(None)
    start_vert.setDistance(0)

    # 优先队列（最小堆）：存储 (到已选集合的距离, 顶点ID)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start_key))
    total_weight = 0  # 最小生成树总权重

    # 2. 核心循环：贪心选择+扩展已选集合
    while priority_queue:
        # 取出到已选集合距离最小的顶点
        current_dist, current_id = heapq.heappop(priority_queue)
        current_vert = graph.getVertex(current_id)

        # 如果已加入已选集合，跳过
        if current_vert.getColor() == 'black':
            continue

        # 加入已选集合，累加权重
        current_vert.setColor('black')
        total_weight += current_dist

        # 扩展：更新邻接顶点到已选集合的最小距离
        for neighbor in current_vert.getConnections():
            if neighbor.getColor() == 'white':
                # 邻接顶点到已选集合的距离 = 当前边的权重
                edge_weight = current_vert.getWeight(neighbor)
                if edge_weight < neighbor.getDistance():
                    neighbor.setDistance(edge_weight)
                    neighbor.setPred(current_vert)  # 记录MST中的前驱
                    heapq.heappush(priority_queue, (edge_weight, neighbor.getId()))

    # 3. 整理结果：前驱字典 + 总权重
    pred_dict = {}
    for vert_id in graph.getVertices():
        pred_vert = graph.getVertex(vert_id).getPred()
        pred_dict[vert_id] = pred_vert.getId() if pred_vert else None

    return pred_dict, total_weight
#================测试代码=====================
# 测试函数
def test_prim():
    # 1. 构建无向带权图
    mst_graph = Graph()
    # 添加无向边：from_key, to_key, weight
    mst_graph.addEdge(0, 1, 2)
    mst_graph.addEdge(0, 2, 5)
    mst_graph.addEdge(1, 2, 1)
    mst_graph.addEdge(1, 3, 7)
    mst_graph.addEdge(2, 3, 1)
    mst_graph.addEdge(2, 4, 3)
    mst_graph.addEdge(3, 4, 1)

    # 2. 执行Prim算法（起点为0）
    pred_dict, total_weight = prim(mst_graph, start_key=0)

    # 3. 输出结果
    print("=== Prim算法结果（最小生成树）===")
    print(f"最小生成树总权重：{total_weight}")
    print("顶点ID → MST中的前驱顶点（可还原MST的边）：")
    for vert_id in sorted(pred_dict.keys()):
        print(f"顶点{vert_id}: {pred_dict[vert_id]}")

# 运行测试
if __name__ == "__main__":
    test_prim()