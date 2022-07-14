"""
变量， 函数， 类， 模块和其他对象起的名字就叫标识符
规则：
    字母， 数字， 下划线_
    不能以数字开头
    不能是python自带的保留字
    我是严格区分大小的
"""

import keyword
print(keyword.kwlist) # 这句代码 输出的是python自带的保留字 在给变量， 函数， 类， 模块和其他对象起名字时是不能使用的，否者会报错

"""
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async',
 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
  'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
   'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""