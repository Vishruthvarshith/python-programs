#find all the factors of a nuber and count the number of factors.
#use the number of factors to check whether the number is prime or not 
n=int(input("enter the number: "))
i=1
c=0
while(i<=n/2):
    if(n%i==0):
        c+=1
        print(n/i)
    i+=1
    print("number of factors: ",c+1)
if(c==1):
    print("it is a prime number")
else:
    print("the number is not prime")