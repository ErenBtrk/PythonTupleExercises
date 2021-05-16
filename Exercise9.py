'''
9. Write a Python program to find the repeated items of a tuple.
'''

tuple1 = (1,2,3,4,5,2,4)
mylist = []

for item in tuple1:
    if(tuple1.count(item) > 1):
        if(not item in mylist):
            mylist.append(item)
            
print(mylist)
