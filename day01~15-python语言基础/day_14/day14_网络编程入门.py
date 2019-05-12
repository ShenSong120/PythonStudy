# '''
# TCP:传输控制协议
# IP:网络协议(身份标识)
# TCP/IP:(四层模型,自上向下为)
#         1.网络接口层
#         2.网络层
#         3.传输层
#         4.应用层
# 网络应用模式:
#         1.C/S:客户端&服务端
#         2.B/S:浏览器&服务器
# HTTP(Hyper-Text Transfer Proctol):
#     超文本传输协议
# '''
# from time import time
# from threading import Thread
# import requests
#
# # 继承Thread类创建自定义的线程类
# class DownloadHanlder(Thread):
#     def __init__(self, url):
#         super().__init__()
#         self.url = url
#
#     def run(self):
#         filename = self.url[self.url.rfind('/')+1:]
#         resp = requests.get(self.url)
#         with open('../TxtFile/'+filename, 'wb') as f:
#             f.write(resp.content)
#
# def main(self):
#     # 通过request模块的get函数获取网络资源
#     # 下面的代码中使用了天行数据接口提供的网络API
#     # 要使用该数据接口需要在天行数据的网站上注册
#     # 然后用自己的key替换掉下面代码中的APIKey即可
#     resp = requests.get('http://api.tianapi.com/meinv/?key=APIKey&num=10')
#     # 将服务器返回的JSON格式的数据解析为字典
#     data_model = resp.json()
#     for mm_dict in data_model['newslist']:
#         url = mm_dict['picUrl']
#         # 通过多线程的方式实现图片下载
#         DownloadHanlder(url).start()
# if __name__=='__main__':
#     main()

'''
TCP套接字
实现一个提供时间日期的服务器
'''
from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime

def main():
    # 1.创建套接字对象并指定使用哪种传输服务
    # family=AF_INET - IPv4地址
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW -原始套接字
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2.绑定IP地址和端口(端口用于区分不同的服务)
    # 同一时间在同一端口上只能绑定一个服务,否则报错
    server.bind(('192.168.1.2', 6789))
    # 开启监听 - 监听客户端连接到服务器
    # 参数512可以理解为连接队列的大小
    server.listen(512)
    print('服务器启动开始监听...')
    while True:
        # 4.通过循环接收客户端的连接并作出相应处理(提供服务)
        # accept方法是一个阻塞方法,如果没有客户端连接到服务
        # 器代码不会向下执行
        # accept方法返回一个元组,其中的第一个元素是客户端
        # 对象,第二个元素是连接到服务器的客户端地址
        # (由IP和端口两部分构成)
        client, addr = server.accept()
        print(str(addr) + '连接到了服务器.')
        # 5.发送数据
        client.send(str(datetime.now()).encode('utf-8'))
        # 6.断开连接
        client.close()

if __name__=='__main__':
    main()