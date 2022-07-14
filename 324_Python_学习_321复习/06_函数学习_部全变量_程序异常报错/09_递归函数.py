def fun(n):
    if n == 1:
        return 1
    else:
        res = n*fun(n-1)
        return res

print(fun(6))

def fin(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fin(n-1)+fin(n-2)

print(fin(9))
print('-----------------')
for i in range(1,10):
    print(fin(i))


"""
720
34
-----------------
1
1
2
3
5
8
13
21
34
"""
