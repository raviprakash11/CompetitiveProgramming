import time
import random
n=int(input("enter the order of matrix:"))
a=[]
b=[]
for i in range(0,n):
	c=[]
	for j in range(0,n):
		c.append(random.randrange(1,100))
	a.append(c)
for j in range(0,n):
	c=[]
	for j in range(0,n):
		c.append(random.randrange(1,100))
	b.append(c)
print(a)
print(b)
z2=[[0 for i in range(n)] for i in range(n)]
def matrix(x,y):
	for i in range(n):
		for j in range(n):
			for k in range(n):
				z2[i][j]=z2[i][j]+(x[i][k]*y[k][j])
	print(z2)
t1=time.time()
matrix(a,b)
t2=time.time()
print("time taken {0}".format(t2-t1))
