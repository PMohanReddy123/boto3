def fun(a):
    return a['name']
b=[
    {'name':'azar','year':1980},
    {'name':'Mohan','year':1996},
    {'name':'Reddy','year':1982},
    {'name':'MD','year':1984}
  ]
b.sort(key=fun)
print(b)