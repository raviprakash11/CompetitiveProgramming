#calculator
print("Select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
ch=int(input("Enter choice(1/2/3/4):"))
a=int(input("Enter first number :"))
b=int(input("Enter second number:"))
if ch==1 :
	sum=a+b
	print(a,"+",b,"=",sum)
elif ch==2:
	sub=a-b
	print(a,"-",b,"=",sub)

	#print("sub of a and b:",sub)
elif ch==3:
	mul=a*b
	print(a,"*",b,"=",mul)

elif ch==4:
	div=a/b
	print(a,"/",b,"=",div)

