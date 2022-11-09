#input a number of four digts and print all the digits one by one and get a sum of of all the digits 
n=int(input("enter the number with four digits: "))
n1=n//1000
print("digit 1: ",n1)
n2=(n-n1*1000)//100
print("digit 2: ",n2)
n3=(n-n1*1000-n2*100)//10
print("digit 3: ",n3)
n4=(n-n1*1000-n2*100-n3*10)
print("digit 4: ",n4)
sum=n1+n2+n3+n4
print("the sum of the numbers are: ",sum)