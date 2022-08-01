
# Imagine you have 2 lists. You have to write such a code so that a new list is 
# made in which the items of both these lists should be there in both the lists.
# repeated values

from builtins import len, print


a= [1, 342, 75, 23, 98]
b= [75, 23, 98, 12, 78, 10, 1] 
i=0
c=[]
while i<len(a):
    if a[i] not in c:
        c.append(a[i])
    if b[i] not in c:
        c.append(b[i])
    i+=1
print(c)