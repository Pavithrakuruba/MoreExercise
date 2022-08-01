# Imagine you have two lists. Now you have to make a new list which should contain
# the elements of both the lists.But it is to be kept in mind that all the elements
#  in both the lists should be there only once. If we have these two lists:
# assending


from builtins import len, print


list1= [1, 5, 10, 12, 16, 20]
list2= [1, 2, 10, 13, 16]
i=0
n=[]
while i<len(list1):
    k=list1[i]
    if k in list2:
        n.append(k)
    i=i+1
print(n)
