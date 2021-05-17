'''
19. Write a Python program to convert a list of tuples into a dictionary.
'''

list1 = [(1,2),(3,4),(5,6),(7,8),(9,10)]

print(dict((x, y) for x, y in list1))

############################################################################################
#create a list
l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
d = {}
for a, b in l:
    d.setdefault(a, []).append(b)
print (d)