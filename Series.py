#w=int(input("enter"))
#s=0
#while w>0:
#	s=s+w;
#	w=w-2;
#print(s)
#fibbo
def fibonacci(n):
	if(n<=1):
		return n
	else:
		return(fibonacci(n-1)+fibonacci(n-2))
n=int(input("netre no of terms:"))
print("fib series")
for i in range(n):
	print(fibonacci(i))
