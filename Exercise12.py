'''
12. Write a Python program to remove an item from a tuple.
'''

tuple1 = (1,2,3,4,5)

tuple1 = list(tuple1)

del(tuple1[3])

tuple1 = tuple(tuple1)

print(tuple1)

