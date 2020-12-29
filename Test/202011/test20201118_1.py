# 类与对象

class Person(object):

    def __init__(self, name, sexual):
        self.name = name
        self.sexual = sexual
        print("init {}".format(self.name))

    def eat(self, foodName="空气"):
        print("{} 吃 {}".format(self.name, foodName))


class Man(Person):

    def __init__(self, name, sexual, voice):
        super().__init__(name, sexual)
        self.voice = voice


p1 = Person("牛顿老师", "男")
print(p1.__dict__)

man1 = Man("牛顿老师", "男", 100)
print(man1.__dict__)



    # # 属性装饰器
    # @property
    # def sexual(self):
    #     return self._sexual

    # # @property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    # @sexual.setter
    # def sexual(self, value):
    #     self._sexual = value