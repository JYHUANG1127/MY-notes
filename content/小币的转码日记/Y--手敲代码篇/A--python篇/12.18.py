class animal(object):
    def __init__(self,year):
        self.age=year
    def get_age(self):
        return self.age
    def set_age(self,nums):
        self.age=nums

class person(animal):
    tag=1
    def __init__(self,name,friends,year):
        animal.__init__(self, year)
        self.name=name
        self.friends=friends
        self.rid=person.tag
        person.tag+=1
    def __str__(self):
        return f'名字：{self.name},年龄：{self.age},朋友:{self.friends},第几个人：{self.rid}'
    def crowds(L):
        d={}
        for i in L:
            d[i.name]=i
        return d
p1=person('弥豆子',['炭治郎','善逸'],14)
print(p1)
p1.set_age(15)
print(p1)
p2=person('炭治郎',['弥豆子','善逸'],15)
p3=person('善逸',['弥豆子','炭治郎'],16)
print(p2)
print(p3)
people=person.crowds([p1,p2,p3])
print("---遍历人群信息---")
for name,friends,age,id in people.items:
    print(f'名字：{name},朋友：{friends},年龄:{age},第几个人:{id}')
print(people)
