import random
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
#用队列来解决约瑟夫环，以热土豆传递为例，用queue来储存所有参加传递土豆的人名，
#按照传递方向依此从队首排到队尾，模拟开始时，只需要让队首的出队，然后加入队尾即可，
#直到传递num次，然后这时队尾的就是最后拥有土豆的
def hotPotato(namelist,num):
    name_list = Queue()
    for name in namelist:
        name_list.enqueue(name)
    while name_list.size() > 1:
        for i in range(num):
            name_list.enqueue(name_list.dequeue())
        name_list.dequeue()
    return name_list.dequeue()
namelist = ['HJY','JHY','HYY','YHH','AFE','DEE','XJ','LFC','HYF']
print(hotPotato(namelist,5))
#用queue来模拟打印机决策，问题的主要前提是：一个小时内可能发生A次打印任务，
#每次任务都是打印1-B张纸，如果选择草稿模式打印，每秒打印C张，但质量较差，
#如果选择正式模式打印，每秒打印D张（C>D），但质量较好，应该采取什么样的策略来使具体时间
#内打印的纸张尽可能的多和质量更好
class Task():
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)
    def getstamp(self):
        return self.timestamp
    def getpages(self):
        return self.pages
    def waittime(self,currenttime):
        return currenttime - self.timestamp
def newprinttask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False
class Printer:
    def __init__(self,ppm):#定义打印机的属性，每分钟打印数量等于ppm，设置默认参数none和0
        self.pagerate = ppm
        self.currenttask = None
        self.timeremaining = 0
    def tick(self):#定义打印一秒
        if self.currenttask != None:
            self.timeremaining -=1
            if self.timeremaining < 0:
                self.currenttask =None
    def busy(self):
        if self.currenttask == None:
            return False
        else:
            return True
    def startnext(self,newtask:Task):
        self.currenttask = newtask
        self.timeremaining = newtask.getpages() * 60 / self.pagerate
def simulation(numseconds,pagesperminute):
    labprinter = Printer(pagesperminute)
    printqueue = Queue()
    waitingtimes = []
    for currentsecond in range(numseconds):
        if newprinttask():
            task = Task(currentsecond)
            printqueue.enqueue(task)
        if (not labprinter.busy()) and (not printqueue.isEmpty()):
            nexttask = printqueue.dequeue()
            waitingtimes.append(nexttask.waittime(currentsecond))
            labprinter.startnext(nexttask)
        labprinter.tick()
    if len(waitingtimes) > 0:
        averagewait = sum(waitingtimes) / len(waitingtimes)
        return print("Average Wait %6.2f secs %3d tasks remaining." %(averagewait,printqueue.size()))
    else:
        return print("no task completed during simulation")

# 测试案例 1：标准场景（1小时，每分钟5页）
print("--- 测试 1：标准场景 ---")
simulation(3600, 0.1)

# 测试案例 2：高性能打印机（1小时，每分钟10页）
# 预期：等待时间应该比测试 1 明显缩短
print("\n--- 测试 2：高性能打印机 ---")
simulation(3600, 100)

# 测试案例 3：极短时间测试（检查是否报错）
print("\n--- 测试 3：极短时间 ---")
simulation(10, 5)
