# Imagine you have a list in which some values ​​are appearing again and again.

# Write such a code by which you create a new list in which the items of this 
# list appear only once. like:

from builtins import len, print


a = ["Rishabh","Rishabh","Abhishek","Rishabh","Divyashish","Divyashish","shreshta"]
i=0
b=[]
while i<len(a):
    c=a[i]
    if c not in b:
        b.append(c)
    i+=1
print(b)


# a= [1, 342, 75, 23, 98]
# b= [75, 23, 98, 12, 78, 10, 1] 
# i=0
# c=[]
# while i<len(a):
#     d=str(a[i])+str(b[i])
#     c.append(d)
#     i+=1
# print(c)