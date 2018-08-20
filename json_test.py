# -*- coding:utf-8 -*-
# author : Keekuun

"""
JSON: 不同语言之间的传递对象
JSON            python  数据类型对应关系

{}              dict
[]              list
"string"        str
123.6           int/float
true/false      True/False
null            None
"""

import json

"""注意py文件名不可用json.py命名，否则回报崔：module 'json' has no attribute 'dumps'"""

# python中的dict
d = {'name': 'Bob', 'age': 20}
# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
dict2json = json.dumps(d)
print(dict2json)  # {"name": "Bob", "age": 20}
print(type(dict2json))  # <class 'str'>

# 把JSON反序列化为Python对象，用loads()或者对应的load()方法，loads()把JSON的字符串反序列化，load()从file-like Object中读取字符串并反序列化
json2dict = json.loads(dict2json)
print(json2dict)  # {'name': 'Bob', 'age': 20}


# json高级用法
# 将Student实例变为一个JSON的{}对象

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


st = Student('Bob', 20, 100)


# 第一种方法,自定义函数
def st2dict(std):
    d = {'name': std.name, 'age': std.age, 'score': std.score}
    return d


std2json1 = json.dumps(st, default=st2dict)
print(std2json1)

# 第二种方法,用类的__dict__方法
# 通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
std2json2 = json.dumps(st, default=lambda obj: obj.__dict__)
print(std2json2)


# 把JSON反序列化为一个Student对象实例，loads()方法转换出dict对象,传入object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))

