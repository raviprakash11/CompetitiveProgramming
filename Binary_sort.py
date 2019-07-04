import time
import random as rand
n=int(input("Enter the array size:"))
list=[i for i in range(n)]
def binary_search(list,key,beg,last):
	while(beg<=last):
		mid=(beg+last)/2
	if(list[mid]==key):
		return key
	elif(list[mid]>key):
		last=mid-1
	elif(list[mid]<key):
		beg=mid+1
def exe_time(list,key,beg,last):
	start=time.time()
	binary_seach(list,key,beg,last)
	end=time.time()
	return(end-start)
beg=0
last=n-1
#best case
mid=(beg+last)/2
print("\n Best case time:{}".format(exe_time(list,mid,beg,last)))
#worst case
print("\n Worst case time:{}".format(exe_time(list,mid,beg,last)))
#avearge case
sum=0
for i in range(100):
	sum =exe_time(list,rand.randrange(1,100),beg,last)
avg=sum/100
print("\n Best case time:{}".format(avg))

