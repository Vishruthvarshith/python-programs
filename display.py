# to diplay number in range 100 to 200 whose sum of digits are even  
a=int(input("enter the starting point: "))
b=int(input("enter the ending  point: "))
list=[]
for i in range(a,b+1):
    i=str(i)
    sum=0
    for j in i:
        j=int(j)
        sum=sum+j
    if(sum%2==0):
        list.append(i)
print("the digits are ",list)