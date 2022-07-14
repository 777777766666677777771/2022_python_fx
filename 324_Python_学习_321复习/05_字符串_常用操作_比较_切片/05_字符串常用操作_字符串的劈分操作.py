s = 'hello world python'
lst = s.split()
print(lst)
s1 = 'hello|world|python'
print(s1.split(sep='|'))
print(s1.split(sep='|', maxsplit=1))

'''rsplit()从右测开始劈分'''
print(s.rsplit())
print(s1.rsplit('|'))
print(s1.rsplit(sep='|', maxsplit=1))

"""
['hello', 'world', 'python']
['hello', 'world', 'python']
['hello', 'world|python']
['hello', 'world', 'python']
['hello', 'world', 'python']
['hello|world', 'python']
"""