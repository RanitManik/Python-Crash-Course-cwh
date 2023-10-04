# This is program 12
# tuples are also immutable like Strings
t = (2, 5, 6, 58, 96, 5)
print(t.count(5))
print(t.index(58))
'''
 t[0] = 89 ==> will give me error that ==>
 tuple objects does not support item assignment
'''
# t[0]=89 will through an error as tuples are immutable
