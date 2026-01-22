#利用Graph解决词梯问题
from collections import deque
import os
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
def buildGraph(word_file):
    g = Graph()
    pattern_dict = {}
    with open(word_file,'r') as f:
        for line in f:
            word = line.strip().lower()
            if len(word) != 4:
                continue
            for i in range(4):
                pattern = word[:i] + '_' + word[i+1:]
                if pattern not in pattern_dict:
                    pattern_dict[pattern] = []
                pattern_dict[pattern].append(word)
    for pattern in pattern_dict:
        word_list = pattern_dict[pattern]
        for i in range(len(word_list)):
            for j in range(i+1,len(word_list)):
                word1 = word_list[i]
                word2 = word_list[j]
                g.addEdge(word1,word2)
    return g
def bfs(start_vert:Vertex):
    start_vert.setColor('gray')
    start_vert.setDistance(0)
    start_vert.setPred(None)
    queue = deque()
    queue.append(start_vert)
    while queue:
        current_vert = queue.popleft()
        for nbr in current_vert.getConnections():
            if nbr.getColor() == 'white':
                nbr.setColor('gray')
                nbr.setDistance(current_vert.getDistance() + 1)
                nbr.setPred(current_vert)
                queue.append(nbr)
        current_vert.setColor('black')
def traverse(target_vert:Vertex):
    path = []
    current_vert = target_vert
    while current_vert is not None:
        path.append(current_vert.id)
        current_vert = current_vert.getPred()
    path.reverse()
    if len(path) == 1:
        print("没有找到可用的词梯路径")
        return []
    else:
        print("词梯路径："," >> ".join(path))
        return path
def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    words_file_path = os.path.join(script_dir,"words.txt")
    try:
        graph = buildGraph(words_file_path)
        print(f"✅单词图构建完成！共加载{graph.numVertices}个4字母单词")
    except FileNotFoundError:
        print("错误： 找不到words.txt文件， 请检查文件路径")
        return
    start_word = input("请输入起始单词（4字母）：").strip().lower()
    target_word = input("请输入目标单词（4字母）：").strip().lower()
    start_vert = graph.getVertex(start_word)
    target_vert = graph.getVertex(target_word)
    if not start_vert:
        print(f"错误：起始单词{start_word}不存在")
        return
    if not target_vert:
        print(f"错误: 目标单词{target_word}不存在")
        return
    for vert_id in graph.getVertices():
        vert = graph.getVertex(vert_id)
        vert.setColor('white')
        vert.setDistance(-1)
        vert.setPred(None)
    bfs(start_vert)
    traverse(target_vert)
if __name__=="__main__":
    main()

