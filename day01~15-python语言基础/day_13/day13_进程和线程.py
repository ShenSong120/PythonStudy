# from multiprocessing import Process
# from os import getpid
# from random import randint
# from time import time, sleep
#
#
# def download_task(filename):
#     print('启动下载进程，进程号[%d].' % getpid())
#     print('开始下载%s...' % filename)
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))
#
#
# def main():
#     start = time()
#     p1 = Process(target=download_task, args=('Python从入门到住院.pdf', ))
#     p1.start()
#     p2 = Process(target=download_task, args=('Peking Hot.avi', ))
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time()
#     print('总共耗费了%.2f秒.' % (end - start))
#
#
# if __name__ == '__main__':
#     main()



# from multiprocessing import Process
# from time import sleep
#
# counter = 0
#
# def sub_task(string):
#     global counter
#     while counter < 10:
#         print(string, end='', flush=True)
#         counter += 1
#         sleep(0.01)
#
# def main():
#     Process(target=sub_task, args=('Ping',)).start()
#     Process(target=sub_task, args=('Pong',)).start()
#
# if __name__ == '__main__':
#     main()
# '''打印PingPongPingPongPingPongPingPongPingPongPingPongPingPongPingPongPingPongPingPong
# 非想要的结果, 程序看起来没什么问题,应该是Pong&Ping
# 各输出五次(一共输出10个单词).但是为什么各自输出10个,
# 这是因为当我们在程序中创建进程的时候,子进程复制了父进
# 程及其所有的数据结构,每个子进程有其独立的内存空间,这
# 也就意味着两个子进程中各有一个counter变量,所以结果也
# 就可想而知了. 要解决这个问题比较简单的办法是使用
# multiprocessing模块中的Queue类,他是可以被多个进程
# 共享的队列,底层是通过管道和信号量(semaphore)机制来
# 实现的.'''


# #创建两个进程#
# from multiprocessing import Process
# import os
#
# def run_proc(name):
#     print('Run child process %s (%s)'%(name, os.getpid()))
#
# if __name__=='__main__':
#     print('Parent process %s.'%os.getpid())
#     p = Process(target=run_proc, args=('test', ))
#     print('Process will start...')
#     p.start()
#     p.join()
#     print('Process end.')


# # #创建多个进程#
# # Pool进程池
# from multiprocessing import Pool
# import os, time, random
#
# def long_time_task(name):
#     print('Run task %s (%s)...'%(name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s run %0.2f second.'%(name, (end-start)))
#
# if __name__=='__main__':
#     print('Parent process %s.'%os.getpid())
#     # 0, 1, 2, 3先执行, 其中前面一个进程执行完毕后执行
#     # 执行进程4, 因为Pool()默认同时开启的进程数位计算机
#     # CPU核数. 当然也可以将Pool()参数设置你想要开启的
#     # 进程数, 例如Pool(5)代表同时可以开启5个进程
#     p = Pool(5)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i, ))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')


# '''
# 进程间通信
# Process之间肯定是需要通信的,操作系统提供了很多机制
# 来实现进程间通信.python的multiprocessing模块包
# 装了底层的机制,提供了Queue\Pipes等多种方式来交换
# 数据.
# 这里以Queue为例,在父进程中创建两个子进程,一个往Queue
# 里面写数据,一个从Queue里读数据：
# '''
# from multiprocessing import Process, Queue
# import os, time, random
#
# # 写数据进程执行的代码
# def write(q):
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...'%value)
#         q.put(value)
#         time.sleep(random.random())
#
# def read(q):
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.'%value)
#
# if __name__=='__main__':
#     # 父进程创建Queue,并传给各个子进程
#     q = Queue()
#     pw = Process(target=write, args=(q, ))
#     pr = Process(target=read,  args=(q, ))
#     # 启动子进程pw, 写入
#     pw.start()
#     # 启动子进程pr, 读取
#     pr.start()
#     # 等待pw结束
#     pw.join()
#     # pr进程里面是死循环,无法等待其结束,只能强行种植
#     pr.terminate()


# '''
# 多线程
# thread低级
# threading高级
# '''
# import time, threading
#
# def loop():
#     print('thread %s is running...'%threading.current_thread().name)
#     n = 0
#     while n<5:
#         n = n+1
#         print('thread %s >>> %s'%(threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s is ended.'%threading.current_thread().name)
# print('thread %s is running...'%threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.'%threading.current_thread().name)


# '''
# 多线程Lock
# '''
# import time, threading
#
# # 假定这是你的银行存款
# balance = 0
# lock = threading.Lock()
# def change_it(n):
#     # 先存后取, 结果应该为零
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_thread(n):
#     for i in range(100000):
#         # 获取锁
#         lock.acquire()
#         try:
#             change_it(n)
#         finally:
#             # 改完后释放锁
#             lock.release()
#
# t1 = threading.Thread(target=run_thread, args=(5, ))
# t2 = threading.Thread(target=run_thread, args=(8, ))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)


# '''
# 多线程
# ThreadLocal
# '''
# import threading
#
# # 创建全局ThreadLocal对象:
# local_school = threading.local()
#
# def process_student():
#     print('Hello, %s (in %s)' % (local_school.student, threading.current_thread().name))
#
# def process_thread(name):
#     # 绑定ThreadLocal的student:
#     local_school.student = name
#     process_student()
#
# t1 = threading.Thread(target= process_thread,
#                       args=('Alice',),
#                       name='Thread-A')
# t2 = threading.Thread(target= process_thread,
#                       args=('Bob',),
#                       name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()


'''
分布式进程
举个例子
如果我们有一个通过Queue通信的多进程程序在同一台机器上运行
,现在由于处理任务的进程任务繁重,希望把发送任务的进程和处理
任务的进程分布到两台机器上,如何实现？
原有的Queue可以继续使用,但是,通过managers模块把Queue
通过网络暴露出去,就可以让其他机器的进程访问了
我们先看服务进程,服务进程负责启动Queue,把Queue注册到网络
上,然后往Queue中写入任务
'''

# 实例见:
# https://www.liaoxuefeng.com
# /wiki/1016959663602400/
# 1017631559645600