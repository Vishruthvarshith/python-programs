a=int(input("enter the value of a: "))
r=int(input("enter the value of r: "))
n=int(input("enter the value of n: "))
list=[]
if(r<=a):
    for i in range(1,n+1):
        t_n=a*r**(i-1)
        list.append(t_n)
        print(list)
        print(t_n)
if(r>1):
    s_n=a*r**(n)/(r-1)
else:
    s_n=a*r**(n)/(1-r)
print(s_n)