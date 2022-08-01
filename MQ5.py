# Factorial of a number is obtained by multiplying all the numbers from 1 to
#  that number together.
#1) For example, the factorial of 3 is 6. Because calculating 1 * 2 * 3 gives 6
#2)The factorial of 4 is 24. Because calculating 1 * 2 * 3 * 4 gives 24

from builtins import input, int, print
a=int(input("enter number:"))
i=1
b=1
while i<=a:
    b=b*i
    i+=1
print(b)


