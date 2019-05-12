'''
'r' 读取(默认)
'w' 写入(会先截断之前的内容)
'x' 写入(如果文件已经存在则会产生异常)
'a' 追加(将内容写入到已有文件的末尾)
'b' 二进制模式
't' 文本模式(默认)
'+' 更新（可读可写）
'''
# # close写法
# def main():
#     f = None
#     try:
#         f = open('../TxtFile/离职.txt', 'r', encoding='utf-8')
#         print(f.read())
#     except FileNotFoundError:
#         print('无法打开指定的文件!')
#     except LookupError:
#         print('指定了未知的编码!')
#     except UnicodeDecodeError:
#         print('读取文件时解码错误!')
#     finally:
#         if f:
#             f.close()

# # with...open 写法
# def main():
#     try:
#         with open('../TxtFile/离职.txt', 'r', encoding='utf-8') as f:
#             print(f.read())
#     except FileNotFoundError:
#         print('无法打开指定的文件!')
#     except LookupError:
#         print('指定了未知的编码!')
#     except UnicodeDecodeError:
#         print('读取文件时解码错误!')


# import time
#
# def main():
#     # 一次性读取整个文件内容
#     with open('../TxtFile/离职.txt', 'r', encoding='utf-8') as f:
#         print(f.read())
#
#     # 通过for-in循环逐行读取
#     with open('../TxtFile/离职.txt', 'r', encoding='utf-8') as f:
#         for line in f:
#             print(line, end='')
#             time.sleep(1)
#     print()
#
#     # 读取文件按行读取到列表中
#     with open('../TxtFile/离职.txt', 'r', encoding='utf-8') as f:
#         lines = f.readlines()
#     print(lines)
#
# if __name__=='__main__':
#     main()

# from math import sqrt
#
# def is_prime(n):
#     '''判断是否素数'''
#     assert n > 0
#     for factor in range(2, int(sqrt(n)+1)):
#         if n % factor == 0:
#             return False
#         return True if n != 1 else False
#
# # 将1-9999直接的素数分别写入三个文件中
# # 1-99之间的素数保存在a.txt中
# # 100-999之间的素数保存在b.txt中
# # 1000-9999之间的素数保存在c.txt中
# def main():
#     file_names = ('../TxtFile/a.txt', '../TxtFile/b.txt', '../TxtFile/c.txt')
#     fs_list = []
#     try:
#         for filename in file_names:
#             fs_list.append(open(filename, 'w', encoding='utf-8'))
#         for number in range(1,10000):
#             if is_prime(number):
#                 if number < 100:
#                     fs_list[0].write(str(number) + '\n')
#                 elif number < 1000:
#                     fs_list[1].write(str(number) + '\n')
#                 else:
#                     fs_list[2].write(str(number) + '\n')
#     except IOError as ex:
#         print(ex)
#         print('写文件时发生错误！')
#     finally:
#         for fs in fs_list:
#             fs.close()
#     print('操作完成！')
#
# if __name__=='__main__':
#     main()


# def main():
#     '''读写二进制文件'''
#     try:
#         with open('../TxtFile/Mac0.jpg', 'rb') as fs1:
#             data = fs1.read()
#             print(type(data))
#         with open('../TxtFile/Mac1.jpg', 'wb') as fs2:
#             fs2.write(data)
#     except FileNotFoundError as e:
#         print('指定的文件无法打开')
#     except IOError as e:
#         print('读写文件时出现出现错误')
#     print('程序执行结束')
#
# if __name__=='__main__':
#     main()


# #JSON#
# '''
# 四个重要函数
# dump  -将python对象按照json格式序列化到文件中
# sumps -将python对象处理成json格式的字符串
# load  -将文件中的json数据反序列化成对象
# loads -将字符串的内容反序列化成python对象
# '''
# import json
#
# def main():
#     my_dict = {
#         'name': '骆昊',
#         'age': 38,
#         'qq': 123456,
#         'friends': ['王大锤', '白元芳'],
#         'cars':[
#             {'brand': 'BYD', 'max_speed': 180},
#             {'brand': 'Audi', 'max_speed': 280},
#             {'brand': 'Benz', 'max_speed': 320},
#         ]
#     }
#     try:
#         with open('../TxtFile/data.json', 'w', encoding='utf-8') as fs:
#             json.dump(my_dict, fs)
#     except IOError as e:
#         print(e)
#     print('保存数据完成')
#
# if __name__=='__main__':
#     main()

import json

# data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
# json = json.dumps(data)
# print(json)

print(json.dumps({'a': 'Runoob', 'b': 7},
                 sort_keys=True,
                 indent=4,
                 separators=(',', ': ')))