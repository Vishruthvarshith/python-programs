n1=int(input("enter the value: "))
n2=int(input("enter the value: "))
c=0
if(n2>n1):
    l=n1
else:
    l=n2
for i in range(1,l+1,1):
    if(n1%i==0 and n2%i==0):
        c+=1
if(c==1):
    print("the numbers are co prime")
else:
    print("the numbers are not co prime")