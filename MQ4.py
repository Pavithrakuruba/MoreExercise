# Take the input of 3 integers in 3 different variables using input.
#  After taking the input print the largest number out of these 3
from builtins import input, int, print


a=int(input("enter number:"))
b=int(input("enter second number:"))
c=int(input("enter thired number:"))
if a>b and a>c:
    print(a,"largest num")
elif b>a and b>c:
    print(b,"largest num")
elif c>a and c>b:
    print(c,"laegest num")