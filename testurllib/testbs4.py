#-*- coding = utf-8 -*-
#@Time : 2021/6/6 10:23
#@Author : lqw
#@File : testbs4.py
#@software : PyCharm

'''
BeautifulSoup将复杂的HTML文档转换成一个复杂的树形结构，每个节点都是python对象，所有对象可以归纳为4种：
- Tag
- NavigableString
- BeautifulSoup
- Comment
'''
from bs4 import BeautifulSoup
import re

file = open("./baidu.html","rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser")

# print(bs.a)
# print(bs.head)
# print(type(bs.head))

#1，Tag 标签及其内容：拿到它所找到的第一个内容

# print(bs.title.string)
# print(type(bs.title.string))

#2,NavigableString：标签里的内容

#拿到a标签里所有的属性
# print(bs.a.attrs)


#print(type(bs))
#3,BeautifulSoup 表示整个文档
#print(bs.name)

# print(bs)



# print(bs.a.string)
# print(type(bs.a.string))


#4，一个特殊的NavigableString，输出的内容不包含注释符号

#---------------------------------------------

#1文档的遍历
#-----遍历文档树-----
#contents:获取Tag的所有子节点，返回一个list
#children:获取Tag的所有子节点，返回一个生成器
# print(bs.head.contents)
# print(bs.head.contents[1])


#2文档的搜索
#（1）find_all()
#字符串过滤：会查找与字符串完全匹配的内容
# t_list = bs.find_all("a")
# print(t_list)


#正则表达式搜索：使用search()方法来匹配内容
#t_list = bs.find_all(re.compile("a"))

#方法 ：传入一个函数（方法），根据函数的要求来搜索
# def name_is_exists(tag):
#     return tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exists)
#
# for item in t_list:
#     print(item)
#
# print(t_list)

#2.kwargs 参数

# t_list = bs.find_all(id="head")
#
# for item in t_list:
#     print(item)
#
# with open("item.txt","wb") as f:
#     f.write(item.encode("utf-8"))
#
# t_list = bs.find_all(class_=True)
#
# for item in t_list:
#     print(item)


# t_list = bs.find_all(text = "hao123")
# t_list = bs.find_all(text = ["hao123","地图","贴吧"])

# t_list = bs.find_all(text= re.compile("\d"))    #应用正则表达式来查找包含特定文本的内容，标签里的字符串
#
# for item in t_list:
#     print(item.string)

# t_list = bs.find_all("a",limit=3)
#
# for item in t_list:
#     print(item)
#

#3.text参数
# t_list = bs.find_all(text = "hao123")
# t_list = bs.find_all(text=["hao123","地图","贴吧"])
# t_list = bs.find_all(text = re.compile("\d"))   #应用正则表达式来查找包含特定文本的内容(标签里的字符串)

#4.limit参数
# t_list = bs.find_all("a",limit=3)
# for item in t_list:
#     print(item)

#css选择器
# t_list = bs.select('title')   #通过标签来查找
# t_list = bs.select(".mnav")   #通过类名来查找
# t_list = bs.select("#u1")     #通过id来查找
# t_list = bs.select("a[class='c-color-gray2 c-font-normal']")
                                #通过属性来查找
# t_list = bs.select("html > head")#通过子标签来查找
t_list = bs.select(".mnav")
print(t_list[0].get_text())
# for item in t_list:
#     print(item)


