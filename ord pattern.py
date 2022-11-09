#A B C D E 
#B C D E 
#C D E 
#D E 
#E
n=int(input("enter the lenght: "))
b=ord('A')
i=0
while(i<n):
    j=0
    while(j<n-i):
        print(chr(b+i+j),end=" ")
        j+=1
    i+=1
    print()