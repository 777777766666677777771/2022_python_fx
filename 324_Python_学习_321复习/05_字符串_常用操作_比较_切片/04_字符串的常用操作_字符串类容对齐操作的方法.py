s = 'hello,python'
print(s.center(20, '*')) # 居中对齐

print(s.ljust(20, '*')) # 左对齐
print(s.ljust(10))
print(s.ljust(20))

print(s.rjust(20,'*')) # 右对齐
print(s.rjust(20))
print(s.rjust(10))

print(s.zfill(20)) # 右对齐， 使用0进行填充
print(s.zfill(10))
print('-8910'. zfill(8))

'''
****hello,python****
hello,python********
hello,python
hello,python        
********hello,python
        hello,python
hello,python
00000000hello,python
hello,python
-0008910
'''