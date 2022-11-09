print("basic salary=25000")
n=int(input("enter the number of cameras sold: "))
price=int(input("enter the price of cameras: "))
bonus=200*n
commision=(n*price)*(12/100)
s=25000+bonus+commision
print("the salary of camera salesperson is",s)