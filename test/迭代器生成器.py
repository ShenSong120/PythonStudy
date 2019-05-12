import time

# ## 计时装饰器
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         func()
#         stop_time = time.time()
#         print('the func run time is %s'%(stop_time-start_time))
#     return wrapper
#
# @timer
# def test1():
#     time.sleep(1)
#     print('in the test1')
#
# test1()

# def timer(func):
#     def warpper(*args, **kwargs):
#         print('打印实参:', args, kwargs)
#         start_time = time.time()
#         func(*args, **kwargs)
#         stop_time = time.time()
#         print('the func run time is %s'%(stop_time-start_time))
#     return warpper
#
# @timer
# def test1(name, age):
#     time.sleep(1)
#     print('in the test1, name is %s, age is %d'%(name, age))
#
# @timer
# def test2(name, age, sex, salary):
#     time.sleep(1)
#     print('in the test2, name is %s, age is %d,\
#      sex is %s, salary is %d'%(name, age, sex, salary))
#
# test1('shensong', 25)
# test2('shensong', 25, 'man', 3000)

# def auth(auth_type):
#     def out_wrapper(func):
#         def wrapper(username, password):
#             if auth_type == 'local':
#                 print('via local certification')
#                 print('I am 包装前')
#                 func(username, password)
#                 print('I am 包装后')
#             elif auth_type == 'ldap':
#                 print('嘻嘻嘻')
#                 func(username, password)
#                 print('via ldap certification')
#         return wrapper
#     return out_wrapper
#
# @auth(auth_type='local')
# def index(username, password):
#     print('welcom to home page <local>', username)
#
# index('yzw', 'secret')


# x = [1, 2, 3]
# y = iter(x)
# for i in range(len(x)):
#     print(next(y))

# def lay_eggs(num):
#     for egg in range(num):
#         res = '蛋%s'%egg
#         yield res
#         print('下完一个蛋')
# laomuji = lay_eggs(10)
# print(laomuji)
# print(laomuji.__next__())
# print(laomuji.__next__())
# print(laomuji.__next__())
# egg_l = list(laomuji)
# print(egg_l)

# def deco(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         next(res)
#         return res
#     return wrapper
#
# @deco
# def eater(name):
#     print('%s ready to eat'%name)
#     food_list=[]
#     while True:
#         food = yield food_list
#         food_list.append(food)
#         print('%s start to eat %s'%(name, food))
#
# g = eater('shensong')
# print(g.send('food1'))
# print(g.send('food2'))