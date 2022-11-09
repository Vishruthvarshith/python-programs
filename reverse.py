a=int(input("enter the number: "))

sum=0
while(a!=0):
    rev=a%10    
    sum=sum*10+rev
    a=a//10
print("the reverse number is: ",sum)

