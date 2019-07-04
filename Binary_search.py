import time
import random
a=[]
n=1000
f=0
l=n-1
m=(f+1)/2
flag=0
for i in range(0,n):
	x=random.randrange(1,100)
	a.append(x)
a.sort()
key=random.randrange(1,100)
start=time.time()
while(f<=1):
	m=(f+1)/2
	if(a[m]<key):
		l=m-1
	elif(a[m]<key):
		f=m+1
	elif(a[m]==key):
		flag=1
	break
if(flag==1):
	print("element found:")
else:
	print("not found:")
end=time.time()
print(end-start)
