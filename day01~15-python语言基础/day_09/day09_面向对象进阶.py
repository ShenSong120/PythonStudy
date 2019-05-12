# class Person(object):
#
#     # 限定当前对象只能绑定括号中的属性
#     __slots__ = ('_name', '_age', '_gender')
#
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     # 静态方法(可以先不用初始化对象,直接调用)
#     @staticmethod
#     def is_valid(status):
#         result = False
#         if status:
#             result = True
#         return result
#
#     # 访问器-getter方法
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#     # 修改器-setter方法
#     @age.setter
#     def age(self, age):
#         self._age = age
#
#     def play(self):
#         if self._age <= 16:
#             print('%s正在玩飞行棋.'%self._name)
#         else:
#             print('%s正在玩斗地主.'%self._name)
#         print('%s is %d age'%(self._name, self._age))
#
# def main():
#     person = Person('王大锤', 12)
#     person.play()
#     person.age = 22
#     # person.age(22)
#     person.play()
#     person._gender = '男'
#
# if __name__=='__main__':
#     main()

# #静态类#
# from time import time, localtime, sleep
#
# class Clock(object):
#     '''
#     数字时钟
#     '''
#     def __init__(self, hour=0, minute=0, second=0):
#         self._hour = hour
#         self._minute = minute
#         self._second = second
#
#     # 定义静态类
#     @classmethod
#     def now(cls):
#         ctime = localtime(time())
#         # 将三个参数传递给__init__中
#         return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
#
#     def run(self):
#         '''走字'''
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0
#
#     def show(self):
#         '''显示时间'''
#         return '%02d:%02d:%02d' % \
#                (self._hour, self._minute, self._second)
#
# def main():
#     clock = Clock.now()
#     while True:
#         print(clock.show())
#         sleep(1)
#         clock.run()
#
# if __name__=='__main__':
#     main()


# #继承#
# class Person(object):
#     '''人'''
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     @property #访问器
#     def name(self):
#         return self._name
#
#     @property  # 访问器
#     def age(self):
#         return self._age
#
#     @age.setter # 修改器
#     def age(self, age):
#         self._age = age
#
#     def play(self):
#         print('%s 正在愉快的玩耍.'%self._name)
#
#     def watch_av(self):
#         if self._age >= 18:
#             print('%s正在观看爱情动作片.'%self._name)
#         else:
#             print('%s只能观看《熊出没》.'%self._name)
#
# class Student(Person):
#     '''学生'''
#     def __init__(self, name, age, grade):
#         super().__init__(name, age)
#         self._grade = grade
#
#     @property
#     def grade(self):
#         return self._grade
#
#     @grade.setter
#     def grade(self, grade):
#         self._grade = grade
#
#     def study(self, course):
#         print('%s的%s正在学习%s.'%(self._grade, self._name, course))
#
# class Teacher(Person):
#     '''老师'''
#     def __init__(self, name, age, title):
#         super().__init__(name, age)
#         self._title = title
#
#     @property
#     def title(self):
#         return self._title
#
#     @title.setter
#     def title(self, title):
#         self._title = title
#
#     def teach(self, course):
#         print('%s%s正在讲%s.'%(self._name, self._title, course))
#
# def main():
#     stu = Student('王大锤', 15, '初三')
#     stu.study('数学')
#     stu.watch_av()
#     t = Teacher('骆昊', 38, '老叫兽')
#     t.teach('python程序设计')
#     t.watch_av()
#
# if __name__=='__main__':
#     main()


# #多态#
# from abc import ABCMeta, abstractmethod
#
# class Pet(object, metaclass=ABCMeta):
#     '''宠物'''
#     def __init__(self, nickname):
#         self._nickname = nickname
#
#     @abstractmethod
#     def make_voice(self):
#         '''发出声音'''
#         pass
#
# class Dog(Pet):
#     '''狗'''
#     def make_voice(self):
#         print('%s: 汪汪汪...'%self._nickname)
#
# class Cat(Pet):
#     '''猫'''
#     def make_voice(self):
#         print('%s: 喵喵喵...' % self._nickname)
#
# def main():
#     pets = [Dog('旺财'), Cat('凯迪'), Dog('大黄')]
#     for pet in pets:
#         pet.make_voice()
#
# if __name__=='__main__':
#     main()

from abc import ABCMeta, abstractmethod
from random import randint, randrange


class Fighter(object, metaclass=ABCMeta):
    """战斗者"""

    # 通过__slots__魔法限定对象可以绑定的成员变量
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        """初始化方法

        :param name: 名字
        :param hp: 生命值
        """
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        """攻击

        :param other: 被攻击的对象
        """
        pass


class Ultraman(Fighter):
    """奥特曼"""

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        """初始化方法

        :param name: 名字
        :param hp: 生命值
        :param mp: 魔法值
        """
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        """究极必杀技(打掉对方至少50点或四分之三的血)

        :param other: 被攻击的对象

        :return: 使用成功返回True否则返回False
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        """魔法攻击

        :param others: 被攻击的群体

        :return: 使用魔法成功返回True否则返回False
        """
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        """恢复魔法值"""
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
            '生命值: %d\n' % self._hp + \
            '魔法值: %d\n' % self._mp


class Monster(Fighter):
    """小怪兽"""

    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
            '生命值: %d\n' % self._hp


def is_any_alive(monsters):
    """判断有没有小怪兽是活着的"""
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False


def select_alive_one(monsters):
    """选中一只活着的小怪兽"""
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(ultraman, monsters):
    """显示奥特曼和小怪兽的信息"""
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


def main():
    u = Ultraman('骆昊', 1000, 120)
    m1 = Monster('狄仁杰', 250)
    m2 = Monster('白元芳', 500)
    m3 = Monster('王大锤', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('========第%02d回合========' % fight_round)
        m = select_alive_one(ms)  # 选中一只小怪兽
        skill = randint(1, 10)   # 通过随机数选择使用哪种技能
        if skill <= 6:  # 60%的概率使用普通攻击
            print('%s使用普通攻击打了%s.' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        elif skill <= 9:  # 30%的概率使用魔法攻击(可能因魔法值不足而失败)
            if u.magic_attack(ms):
                print('%s使用了魔法攻击.' % u.name)
            else:
                print('%s使用魔法失败.' % u.name)
        else:  # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
            if u.huge_attack(m):
                print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        if m.alive > 0:  # 如果选中的小怪兽没有死就回击奥特曼
            print('%s回击了%s.' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms)  # 每个回合结束后显示奥特曼和小怪兽的信息
        fight_round += 1
    print('\n========战斗结束!========\n')
    if u.alive > 0:
        print('%s奥特曼胜利!' % u.name)
    else:
        print('小怪兽胜利!')


if __name__ == '__main__':
    main()