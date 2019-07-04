def make_set(x):
	x.parent=x
	x.rank=0
def find_set(x):
	if(x!=x.parent):
		x=find_set(x.parent)
	return x
def union(x,y):
	xroot=find_set(x)
	yroot=find_set(y)
	if(xroot==yroot):
		print("cycle:")
	elif(xroot.rank<yroot.rank):
		xroot.parent=yroot
		print("node will be:"+xroot.parent)
	else:
		xroot.parent=yroot
		yroot.rank=yroot.rank+1
		print("node will be:"+yroot.parent)

x=[]
y=[]
make_set(x)
find_set(x)
union(x,y)
