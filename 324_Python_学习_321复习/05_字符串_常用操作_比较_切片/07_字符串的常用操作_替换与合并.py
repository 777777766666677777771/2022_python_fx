s = 'hello,Python'
print(s.replace('Python', 'JAVA')) # 替换字符串
s1 = 'hello,Python,Python,Python'
print(s1.replace('Python','JAVA',2))

lst = ['hello', 'java', 'Python'] # 合并字符串
print('|'.join(lst))
print(''.join(lst))

t = ('hello', 'Java', 'Python')
print(''.join(t))

print('*'.join('Python'))

"""
hello,JAVA
hello,JAVA,JAVA,Python
hello|java|Python
hellojavaPython
helloJavaPython
P*y*t*h*o*n
"""