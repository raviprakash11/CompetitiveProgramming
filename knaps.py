def sort(a,n):
	for i in range(n):
		for j in range(n):
			if(a[i]<a[j]):
				temp=a[j]
				a[j]=a[i]
				a[i]=temp

def knp(weight,profit,capacity,n):
	x=[]
	tp=0
	u=capacity
	x=[ 0 for i in range(n)]
	for i in range(n):
		if(weight[i]>u):
			break
		else:
			x[i]=1
			tp=tp+profit[i]
			u=u-weight[i]
	if(i<n):
		n[i]=u/weight[i]
	tp=tp+(x[i]*profit[i])
	print("max profit is{}".format(tp))
weight=[]
profit=[]
ratio=[]
n=int(input("Enter the no of item:"))
capacity=int(input("enter the max weight knapsack:"))
for i in range(n):
	v=int(input("Enter the profit:"))
	profit.append(v)
	w=int(input("enter the wieght:"))
	weight.append(w)
	r=v/w
	ratio.append(r)
sort(ratio,n)
sort(weight,n)
sort(profit,n)
knp(weight,profit,capacity,n)
