items = ['Fruits', 'Books', 'Others']
prices = [96,78,65,100,120]

d = {items.upper():prices for items, prices in zip(items,prices)}
print(d)

"""{'FRUITS': 96, 'BOOKS': 78, 'OTHERS': 65}"""