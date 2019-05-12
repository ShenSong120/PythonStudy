# '''
# ex1
# #验证输入用户名和QQ号
# 是否有效并给出对应提示信息#
# 要求: 用户名由字母/数字/下划线构成长度6-20字符
#      QQ号5-12位数字(首位不能为0)
# '''
# import re
#
# def main():
#     user_name = input('请输入用户名:')
#     qq = input('请输入QQ号:')
#     # match函数的第一个参数是正则表达式字符串或正则表达式对象
#     # 第二个参数是要跟正则表达式做匹配的字符串对象
#     m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', user_name)
#     print(m1)
#     if not m1:
#         print('请输入有效的用户名')
#     m2 = re.match(r'^[1-9]\d{4,11}$', qq)
#     print(m2)
#     if not m2:
#         print('请输入有效的QQ号')
#     if m1 and m2:
#         print('你输入的信息是有效的')
# if __name__=='__main__':
#     main()


# '''
# ex2
# 从一段文字中提取出国内手机号码
# '''
# import re
#
# def main():
#     # 创建正则表达式
#     # 使用前瞻和回顾保证手机号前后不应该出现数字
#     pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
#     sentence = '''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
#     不是15600998765，也不是110或119，王大锤的手机号才是15600998765。
#     '''
#     # 查找所有匹配并保存到一个列表
#     my_list = re.findall(pattern, sentence)
#     print(my_list)
#     print('----------华丽的分割线----------')
#     # 通过迭代器取出匹配对象并获得匹配的内容
#     for temp in pattern.finditer(sentence):
#         print(temp.group())
#     print('----------华丽的分割线----------')
#     m = pattern.search(sentence)
#     while m:
#         print(m.group())
#         m = pattern.search(sentence, m.end())
#
# if __name__=='__main__':
#     main()


# '''
# ex3
# 替换字符串中不良内容
# 说明:
#     re模块的正则表达式相关函数中都有一个flags参数,
#     它代表了正则表达式的匹配标记,
#     可以通过该标记来指定匹配时
#     是否忽略大小写/是否多行匹配/是否显示调试信息等
#     如果需要位flags参数指定多个值,
#     可以使用按位或运算符进行叠加,如flags=re.I | re.M
# '''
# import re
# def main():
#     sentence = '你丫是傻叉吗？我操你大爷的.Fuck you.'
#     purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔', '*', sentence, flags=re.IGNORECASE)
#     print(purified)
#
# if __name__=='__main__':
#     main()


'''
ex4
拆分长字符串
'''
import re
def main():
    poem = '床前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。, .]', poem)
    print(sentence_list)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)

if __name__=='__main__':
    main()