import time as time
import random
list=[]
n=int(input("Enter the Size of Array:"))
for i in range(n):
	x=random.randrange(1,100,1)
	list.append(x)
print(list)
key=int(input("enter the key:"))
def linear(list,key):
	for i in range(n):
		if(list[i]==key):
			return key
def exe_linear(list,key):
	start=time.time()
	linear(list,key)
	end=time.time()
	deff=end-start
	return(deff)
print("key is:",key)
print("time is:",time)
