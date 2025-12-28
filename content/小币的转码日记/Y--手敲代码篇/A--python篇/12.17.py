#ITERATION
def factorial_item(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i
        print(prod)
    return prod
#RECURSION
def fact_recur(n):
    if n==1:
        return 1
    else:
        print(n*fact_recur(n-1))
        return n*fact_recur(n-1)
print(factorial_item(3))
print(fact_recur(3))
def fib_efficient(n,d):
    if n in d:
        return d[n]
    else:
        ans=fib_efficient(n-1,d)+fib_efficient(n-2,d)
        d[n] = ans
        return ans
d = {1:1,2:1}
print(fib_efficient(6,d))

class Pokemon(object):
    def __init__(self,name:str,hp:int):
        self.name = name
        self.hp = hp
    def __str__(self):
        return "宝可梦:"+self.name+",血量："+str(self.hp)
    def attack(self,other):
        other.hp -=10
        print(self.name+"攻击了"+ other.name +'!')
a = Pokemon("皮卡丘",100)
b = Pokemon("杰尼龟",100)
print("---战斗前---")
print(a)
print(b)
print("---战斗中---")
a.attack(b)
b.attack(a)
a.attack(b)
b.attack(a)
print("---战斗后---")
print(a)
print(b)