import time
import random
def trivial(a,b,n):
	c=[[0 for i in range(n)] for i in range(n)]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				c[i][j]+=a[i][k]*b[k][j]
	return c
def add(a,b,n):
	c=[[0 for i in range(n)] for i in range(n)]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				c[i][j]=a[i][j]+b[i][j]
	return c
def sub(a,b,n):
	c=[[0 for i in range(n)] for i in range(n)]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				c[i][j]=a[i][j]-b[i][j]
	return c
def copy (a,r1,r2,c1,c2):
	return[[a[i][j] for j in range(c1,c2)] for i in range(r1,r2)]
def stra(x,y,n):
	if n==1:
		return [[x[0][0]*y[0][0]]]
	else:
		mid=int(n/2)
		a11=copy(x,0,mid,0,mid)
		a12=copy(x,0,mid,mid,n)
		a21=copy(x,mid,n,0,mid)
		a22=copy(x,mid,n,mid,n)
		b11=copy(x,0,mid,0,mid)
		b12=copy(x,0,mid,mid,n)
		b21=copy(x,mid,n,0,mid)
		b22=copy(x,mid,n,mid,n)

		p1=stra(a11,sub(b12,b22,mid),mid)
		p2=stra(add(a11,a12,mid),b22,mid)
		p3=stra(add(a21,a22,mid),b11,mid)
		p4=stra(a22,sub(b21,b11,mid),mid)
		p5=stra(add(a11,a22,mid),add(b11,b22,mid),mid)
		p6=stra(sub(a12,a22,mid),add(b21,b22,mid),mid)
		p7=stra(sub(a11,a21,mid),add(b11,b12,mid),mid)

		c1=add(p5,add(sub(p4,p2,mid),p6,mid),mid)
		c2=add(p1,p2,mid)
		c3=add(p3,p4,mid)
		c4=sub(add(p5,p1,mid),add(p3,p7,mid),mid)

		result=[[0 for i in range(n)] for j in range(n)]
		for i in range(mid):
			for j in range(mid):
				result[i][j]=c11[i][j]
				result[i][j+mid]=c12[i][j]
				result[i+mid][j]=c21[i][j]
				result[i+mid][j+mid]=c22[i][j]
			return result
n=int(input("enter the size:"))
list1=[[random.randrange(0,10) for j in range(n)] for j in range(n)]
list2=[[random.randrange(0,10) for j in range(n)] for j in range(n)]
#start=time.time()
#r1=trivial(list1,list2,n)
#end=time.time()
start2=time.time()
r2=stra(list1,list2,n)
end2=time.time()
print("matrix1:")
for x in list1:
	for y in x:
		print(y,end=' ')
	print()
print("matrix2:")
for x in list2:
	for y in x:
		print(y,end=' ')
	print()
print("result 1:")
for x in r1:
	for y in x:
		print(y,end=' ')
	print()
#print("result 2:")
#for x in r2:
#	for y in x:
#		print(y,end=' ')
#	print()
#print("time taken for trivials:{0}:".format(end-start))
print("time taken for strassen:{0}:".format(end2-start2))
