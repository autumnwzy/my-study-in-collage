ls = {'num1':2,'num2':3,'UK':'newyork'}
print(ls['num2'])
print(ls.keys())
print(ls.values())
print(ls.items())
print('num1' in ls)
print(ls.get('num3',0))
a = ls.popitem()
print(a)
