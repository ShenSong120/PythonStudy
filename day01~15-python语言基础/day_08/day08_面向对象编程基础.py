class Person(object):

    # 限定当前对象只能绑定括号中的属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器-getter方法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # 修改器-setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.'%self._name)
        else:
            print('%s正在玩斗地主.'%self._name)
        print('%s is %d age'%(self._name, self._age))

def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    # person.age(22)
    person.play()
    person._gender = '男'

if __name__=='__main__':
    main()