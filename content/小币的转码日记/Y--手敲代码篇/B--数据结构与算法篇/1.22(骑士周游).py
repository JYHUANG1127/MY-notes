class Vertex():
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.distance = -1
        self.pred = None
    def addNeighbor(self,nbr,weight = 1):
        self.connectedTo[nbr] = weight
    def getConnections(self):
        return list(self.connectedTo.keys())
    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color = color
    def getDistance(self):
        return self.distance
    def setDistance(self,D):
        self.distance = D
    def getPred(self):
        return self.pred
    def setPred(self,vert):
        self.pred = vert
    def __str__(self):
        return f"Vertex({self.id}) connected to:{[n.id for n in self.connectedTo.keys()]}"
class Graph():
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    def addVertex(self,key):
        x = self.vertList.get(key)
        if not x:
            new_vertex = Vertex(key)
            self.vertList[key] = new_vertex
            self.numVertices += 1
            return new_vertex
        return x
    def getVertex(self,key):
        need_vertex = self.vertList.get(key)
        return need_vertex
    def addEdge(self,fromkey,tokey,weight = 1):
        fromvert = self.vertList.get(fromkey)
        tovert = self.vertList.get(tokey)
        if not fromvert:
            fromvert = self.addVertex(fromkey)
        if not tovert:
            tovert = self.addVertex(tokey)
        fromvert.addNeighbor(tovert,weight)
        tovert.addNeighbor(fromvert,weight)
    def getVertices(self):
        return list(self.vertList.keys())
def pos_to_id(row,col,n):
    if 0 <= row < n and 0 <= col < n:
        vertex_id = row*n + col
        return vertex_id
    return None
def id_to_pos(vertex_id,n):
    if 0 <= vertex_id < n**2:
        row = vertex_id // n
        col = vertex_id % n
        return (row,col)
    return None
def generate_legal_moves(row,col,n):
    move_offsets = [(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2),(-2,1),(-2,-1)]
    legal_moves = []
    for dr,dc in move_offsets:
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < n and 0 <= new_col < n:
            legal_moves.append((new_row,new_col))
    return legal_moves
def build_knight_graph(n):
    knight_graph = Graph()
    for row in range(n):
        for col in range(n):
            current_id = pos_to_id(row,col,n)
            knight_graph.addVertex(current_id)
            legal_moves = generate_legal_moves(row,col,n)
            for (new_row,new_col) in legal_moves:
                target_id = pos_to_id(new_row,new_col,n)
                knight_graph.addEdge(current_id,target_id)
    return knight_graph
def knight_tour(n,start_row,start_col):
    graph = build_knight_graph(n)
    start_id = pos_to_id(start_row,start_col,n)
    start_vert = graph.getVertex(start_id)
    if not start_vert:
        print("起始位置非法！")
        return None
    path = []
    if knight_tour_dfs(start_vert,1,path,n):
        path_pos = [id_to_pos(v_id,n) for v_id in path]
        print(f"找到骑士周游路径！路径长度：{len(path_pos)}")
        print("路径坐标：",path_pos)
        return path_pos
    else:
        print("未找到骑士周游路径！")
        return None
def knight_tour_dfs(current_vert:Vertex,path_length,path:list,n):
    current_vert.setColor('gray')
    path.append(current_vert.id)
    if path_length == n**2:
        return True
    for next_vert in current_vert.getConnections():
        if next_vert.getColor() == 'white':
            if knight_tour_dfs(next_vert,path_length + 1,path,n):
                return True
    path.pop()
    current_vert.setColor('white')
    return False
def order_by_warnsdorff(current_vert:Vertex,n):
    def count_legal_moves(vert:Vertex):
        count = 0
        for nbr in vert.getConnections():
            if nbr.getColor() == 'white':
                count += 1
        return count
    unvisited_neighbors = [v for v in current_vert.getConnections() if v.getColor() == 'white']
    unvisited_neighbors.sort(key = count_legal_moves)
    return unvisited_neighbors
def knight_tour_warnsdorff(current_vert:Vertex,path_length,path:list,n):
    current_vert.setColor('gray')
    path.append(current_vert.id)
    if path_length == n**2:
        return True
    sorted_neighbors = order_by_warnsdorff(current_vert,n)
    for next_vert in sorted_neighbors:
        if knight_tour_warnsdorff(next_vert,path_length + 1,path,n):
            return True
    path.pop()
    current_vert.setColor('white')
    return False
def knight_tour_warnsdorff_entry(n,start_row,start_col):
    graph = build_knight_graph(n)
    start_id = pos_to_id(start_row,start_col,n)
    start_vert = graph.getVertex(start_id)
    if not start_vert:
        print("起始位置非法！")
        return None
    path = []
    if knight_tour_warnsdorff(start_vert,1,path,n):
        path_pos = [id_to_pos(v_id,n) for v_id in path]
        print(f"找到骑士周游路径（warnsdorff优化）！路径长度：{len(path_pos)}")
        print("路径坐标",path_pos)
        return path_pos
    else:
        print("未找到骑士周游路径")
        return None
#======================测试代码==================
def main_knight_tour():
    # 1. 输入测试参数
    try:
        n = int(input("请输入棋盘边长（比如5/8）：").strip())
        start_row = int(input("请输入起始行号（0~{}）：".format(n-1)).strip())
        start_col = int(input("请输入起始列号（0~{}）：".format(n-1)).strip())
    except ValueError:
        print("错误：请输入整数！")
        return
    
    # 2. 校验起始位置合法性
    if not (0 <= start_row < n and 0 <= start_col < n):
        print(f"错误：起始位置({start_row},{start_col})超出{n}×{n}棋盘范围！")
        return
    
    # 3. 选择算法
    algo_choice = input("请选择算法（1=朴素DFS，2=Warnsdorff优化）：").strip()
    
    # 4. 运行对应算法
    if algo_choice == "1":
        print("\n=== 运行朴素DFS版骑士周游 ===")
        # 朴素DFS仅适合小棋盘（n≤5），n≥6会极慢
        if n > 5:
            print("⚠️ 警告：朴素DFS在n>5时会极慢，建议改用Warnsdorff优化！")
        result = knight_tour(n, start_row, start_col)
    elif algo_choice == "2":
        print("\n=== 运行Warnsdorff优化版骑士周游 ===")
        result = knight_tour_warnsdorff_entry(n, start_row, start_col)
    else:
        print("错误：请输入1或2选择算法！")
        return
    
    # 5. 输出结果（可选）
    if result:
        print("\n✅ 测试完成！")

# 运行测试主函数
if __name__ == "__main__":
    main_knight_tour()