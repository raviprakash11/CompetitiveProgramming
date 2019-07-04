import random
import time
a=[]
n=int(input("Enter the limit:"))
def Bubble_sort(a,n):
	for i in range(n):
		a.append(random.randrange(1,100))
	m=len(a)
	start=time.time()
	flag=0
	for i in range(0,m-1):
		for j in range(0,m-i-1):
			if(a[j]>a[j+1]):
				temp=a[j]
				a[j]=a[j+1]
				a[j+1]=temp
				flag=1
	end=time.time()
	exe=end-start
	return exe
#insertion sort
def insertion_sort(a,n):
	for p in range(n):
		a.append(random.randrange(1,100))
	start=time.time()
	n=len(a)
	for m in range(0,n-1):
		key=a[m]
		i=m-1
		while(i>0 & a[i]>key):
			a[j+1]=a[i]
			i=i-1
			a[i+1]=key
	end=time.time()
	ti=end-start
	return ti
#selection sort
def selection_sort(a,n):
	for i in range(n):
		a.append(random.randrange(1,100))
	start=time.time()
	m=len(a)
	for i in range(0,m-1):
		min=i
	for j in range(0,m-i-1):
		if(a[j]>a[min]):
			min=j
	if min==i:
		temp=a[i]
		a[i]=a[min]
		a[min]=temp
	end=time.time()
	total=end-start
	return total
print("1.best 2.worst 3.Avg")
ch=input("enter your choice:")
if ch=='1':
	a.sort()
	x=Bubble_sort(a,n)
	y=insertion_sort(a,n)
	z=selection_sort(a,n)
	print("execution time is {}".format(x))
	print("execution time is {}".format(y))
	print("execution time is {}".format(z))
#continue for Bubble_sort , insertion_sort and selection_sort
elif ch=='2':
	a.sort()
	a.reverse()
	a.sort()
	x=Bubble_sort(a,n)
	y=insertion_sort(a,n)
	z=selection_sort(a,n)
	print("execution time is {}".format(x))
	print("execution time is {}".format(y))
	print("execution time is {}".format(z))
elif ch=='3':
	a.sort()
	x=Bubble_sort(a,n)
	y=insertion_sort(a,n)
	z=selection_sort(a,n)
	print("execution time is {}".format(x))
	print("execution time is {}".format(y))
	print("execution time is {}".format(z))
