parent=dict()
rank=dict()
def MAKE_SET(x):
	parent[x]=x
	rank[x]=0
def FIND_SET(x):
	if(parent[x]!=x):
		parent[x]=FIND_SET(parent[x])
	return parent[x]
def UNION(x,y):
	xroot=FIND_SET(x)
	yroot=FIND_SET(y)
	if(xroot!=yroot):
		if(rank[xroot]>rank[yroot]):
			parent[yroot]=xroot
		else:
			parent[xroot]=yroot
		if(rank[xroot]==rank[yroot]):
			rank[yroot]+=1
def MST_KRUSKAL(graph):
	for x in graph['xs']:
		MAKE_SET(x)
		mst=set()
		edge=list(graph['edge'])
		edge.sort()
	for e1 in edge:
		weight,x,y=e1
		if(FIND_SET(x)!=FIND_SET(y)):
			UNION(x,y)
			mst.add(e1)
	return sorted(mst)
graph={'xs':['a','b','c','d','e'],'edge': set([(2,'a','e'),(8,'a','b'),(3,'b','d'),(10,'c','d'),(20,'e','c')])}
print(MST_KRUSKAL(graph))
