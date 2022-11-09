#area of triangle
import math

a=int(input("enter the value: "))
b=int(input("enter the value: "))
c=int(input("enter the value: "))
#d=int(input("enter the option: "))


s=(a+b+c)/2
area=math.sqrt((s*(s-a)*(s-b)*(s-c)))
print(area)



#0.5*a*b*math.sin(c) formula when angle i not given 