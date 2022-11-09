s1=float(input("enter the lenght of side: "))
s2=float(input("enter the lenght of side: "))
s3=float(input("enter the lenght of side: "))
s4=float(input("enter the lenght of side: "))
d1=float(input("enter the lenght of diagonal: "))
d2=float(input("enter the lenght of diagonal: "))
if((s1==s2==s3==s4) and (d1==d2)):
    print("the quadrilateral is a sqaure")
elif((s1==s2==s3==s4) and (d1!=d2)):
    print("the quadrilateral is a rhombus")
elif((s1==s3)and(s2==s4)and(d1==d2)and (d1*d1)==(s1*s1)+(s2*s2)):
    print("the quadrilateral is a rectangle")
elif((s1==s3)and(s2==s4)and(d1==d2) and (d1*d1)!=(s1*s1)+(s2*s2)):
    print("the quadrilateral is a parallelogram")
else:
    print("it is not a quadrilateral")