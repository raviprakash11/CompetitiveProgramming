import time
import random as rand
n=int(input("Enter the arrary size:"))
list=[i for i in range(n)]
list_rand=[rand.randrange(1,100,1) for i in range(n)]
def Linear_search(list,key):
	for i in list:
		if(i==key):
			return key
def exe_time(list,key):
	start=time.time()
	Linear_search(list,key)
	end=time.time()
	return (end-start)
#best case
print("\nworst case time :{}".format(exe_time(list,0)))
#worst case
print("\nbest case time :{}".format(exe_time(list,n-1)))
#average case
sum=0
for i in range(100):
	sum=exe_time(list_rand,rand.randrange(1,1000))
avg=sum/100
print("\nAvearge case time :{}".format(avg))
