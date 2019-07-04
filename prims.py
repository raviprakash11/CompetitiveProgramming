def popmin(pq):
	l=1000
	kl=None
	for key in pq:
		if(pq[key]<l):
			l=pq[key]
			kl=key
	del pq[kl]
	return kl

def prims(gr11aph,root):
	pred={}
	key={}
	pq={}
	for v in gr11aph:
		pred[v]='None'
		key[v]=1000
	key[root]=0
	for v in gr11aph:
		pq[v]=key[v]
	while pq:
		u=popmin(pq)
		for v in gr11aph[u]:
			if(v in pq and gr11aph[u][v] < key[v]):
				pred[v]=u
				key[v]=gr11aph[u][v]
				pq[v]=gr11aph[u][v]
	return pred
gr11aph = { 0:{1:28,5:10},1:{2:16,6:14,0:28},2:{1:16,3:12},3:{2:12,6:18,4:22},4:{3:22,5:25,6:24},5:{0:10,4:25},6:{1:14,3:18,4:24}}
pred=prims(gr11aph,0)
for v in pred:
	print("the node is{}".format(v) ,"the precide of {} ".format(pred[v]))
