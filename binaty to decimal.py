a=int(input("enter the number: "))
b=list()
final_value=0
while(a!=0):
    rev=a%2
    b.append(rev)
    a=a//2
b.reverse()
print(b)
