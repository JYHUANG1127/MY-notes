import turtle
'''
def tree(branch_len):
    if branch_len >5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len-15)
        t.left(40)
        tree(branch_len-15)
        t.right(20)
        t.backward(branch_len)
t = turtle.Turtle()
t.pensize(2)
t.pencolor("green")
tree(75)
t.hideturtle()
turtle.done()
'''
'''
import turtle
def sierpinski(degree,points):
    colormap = ['green','red','blue','white','yellow','orange']
    drawTriangle(points,colormap[degree])
    if degree > 0:
        sierpinski(degree-1,{'left':points['left'],'top':getMid(points['left'],points['top']),'right':getMid(points['left'],points['right'])})
        sierpinski(degree-1,{'left':getMid(points['left'],points['top']),'top':points['top'],'right':getMid(points['top'],points['right'])})
        sierpinski(degree-1,{'left':getMid(points['left'],points['right']),'top':getMid(points['top'],points['right']),'right':points['right']})
def drawTriangle(points,color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()
def getMid(p1,p2):
    return ((p1[0] + p2[0])/2,(p1[1] + p2[1])/2)
t = turtle.Turtle()
points = {'left':(-200,-100),'top':(0,200),'right':(200,-100)}
sierpinski(5,points)
turtle.done()
'''
"""
def moveTower(height,fromPole,withPole,toPole):
    if height >=1:
        moveTower(height - 1,fromPole,toPole,withPole)
        moveDisk(fromPole,toPole)
        moveTower(height - 1,withPole,fromPole,toPole)
def moveDisk(p1,p2):    # 打印“从哪个柱子移动1个盘子到哪个柱子”的步骤（核心是记录单个盘子的移动）
    print(f"将盘子从 {p1} 移动到 {p2}")
moveTower(5,"1#","2#","3#")
#可视化过程，豆包写的，豆包好牛
import turtle
import time

# ===================== 可视化初始化 =====================
# 画布设置
screen = turtle.Screen()
screen.title("汉诺塔可视化（5个盘子）")
screen.setup(width=800, height=600)
screen.bgcolor("white")

# 柱子参数（位置、大小、颜色）
POLE_WIDTH = 20    # 柱子宽度
POLE_HEIGHT = 200  # 柱子高度
POLE_COLOR = "brown"
POLE_POS = {       # 三个柱子的X坐标（对应1#、2#、3#）
    "1#": -200,
    "2#": 0,
    "3#": 200
}

# 盘子参数（大小、颜色）
DISK_HEIGHT = 20          # 所有盘子高度一致
DISK_WIDTH_BASE = 40      # 最小盘子的宽度
DISK_WIDTH_INCREMENT = 20 # 每个大一号盘子增加的宽度
DISK_COLORS = ["red", "orange", "yellow", "green", "blue"] # 盘子颜色（对应1-5号盘子）


# ===================== 绘制柱子 =====================
def draw_poles():
    pole_pen = turtle.Turtle()
    pole_pen.speed(0)  # 最快速度绘制
    pole_pen.hideturtle()
    pole_pen.penup()
    
    for pole_name in POLE_POS:
        x = POLE_POS[pole_name]
        # 画柱子（矩形）
        pole_pen.goto(x - POLE_WIDTH/2, 0)
        pole_pen.pendown()
        pole_pen.color(POLE_COLOR)
        pole_pen.begin_fill()
        for _ in range(2):
            pole_pen.forward(POLE_WIDTH)
            pole_pen.left(90)
            pole_pen.forward(POLE_HEIGHT)
            pole_pen.left(90)
        pole_pen.end_fill()
        pole_pen.penup()

draw_poles()  # 先画出三个柱子


# ===================== 初始化盘子（用turtle对象表示） =====================
# 存储每个盘子的turtle对象（key=盘子大小，1=最小，5=最大）
disks = {}
# 存储每个柱子上的盘子（栈结构：列表最后一个元素是“最上面的盘子”）
poles = {
    "1#": [5, 4, 3, 2, 1],  # 初始：5个盘子在1#柱子（大的在下）
    "2#": [],
    "3#": []
}

# 创建盘子的图形对象
for size in range(1, 6):
    disk = turtle.Turtle()
    disk.shape("square")  # 用正方形表示盘子
    # 调整盘子大小：turtle默认正方形是20x20，所以按比例拉伸
    disk_width = DISK_WIDTH_BASE + (size - 1) * DISK_WIDTH_INCREMENT
    disk.shapesize(stretch_wid=DISK_HEIGHT/20, stretch_len=disk_width/20)
    disk.color(DISK_COLORS[size-1])  # 对应颜色
    disk.penup()
    disks[size] = disk  # 存入盘子字典


# ===================== 把初始盘子放到1#柱子上 =====================
def place_initial_disks():
    pole_name = "1#"
    x = POLE_POS[pole_name]
    # 逐个放置盘子（从大到小，叠在柱子上）
    for idx, size in enumerate(poles[pole_name]):
        # 计算盘子的Y坐标（每个盘子叠在之前的盘子上方）
        y = idx * DISK_HEIGHT + DISK_HEIGHT/2  # 中心在Y位置
        disks[size].goto(x, y)

place_initial_disks()  # 放置初始盘子


# ===================== 可视化的moveDisk（移动盘子图形） =====================
def moveDisk(fromPole, toPole):
    # 1. 从源柱子取出最上面的盘子
    disk_size = poles[fromPole].pop()
    disk = disks[disk_size]
    
    # 2. 获取源柱子和目标柱子的坐标
    from_x = POLE_POS[fromPole]
    to_x = POLE_POS[toPole]
    
    # 3. 动画步骤1：把盘子移到“源柱子上方”（高于柱子）
    disk.goto(from_x, POLE_HEIGHT + DISK_HEIGHT)
    time.sleep(0.5)  # 暂停0.5秒，方便观看
    
    # 4. 动画步骤2：把盘子平移到“目标柱子上方”
    disk.goto(to_x, POLE_HEIGHT + DISK_HEIGHT)
    time.sleep(0.5)
    
    # 5. 动画步骤3：把盘子下移到“目标柱子的合适位置”
    new_y = len(poles[toPole]) * DISK_HEIGHT + DISK_HEIGHT/2
    disk.goto(to_x, new_y)
    time.sleep(0.5)
    
    # 6. 把盘子记录到目标柱子的盘子列表中
    poles[toPole].append(disk_size)


# ===================== 汉诺塔递归逻辑（和之前一致） =====================
def moveTower(height, fromPole, withPole, toPole):
    if height >= 1:
        # 步骤1：把上面height-1个盘子移到辅助柱
        moveTower(height - 1, fromPole, toPole, withPole)
        # 步骤2：移动当前最下面的盘子（调用可视化的moveDisk）
        moveDisk(fromPole, toPole)
        # 步骤3：把辅助柱的height-1个盘子移到目标柱
        moveTower(height - 1, withPole, fromPole, toPole)


# ===================== 启动可视化移动 =====================
moveTower(5, "1#", "2#", "3#")  # 5个盘子从1#→3#，借助2#

turtle.done()  # 保持画布显示（避免运行后直接关闭）
"""