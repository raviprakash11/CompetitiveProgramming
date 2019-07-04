def sorting():
	for i in range(n):
		for j in range(n-i-1):
			if(f[i]>f[j+1]):
				temp=f[j]
				f[j]=f[j+1]
				f[j+1]=temp
				temp=s[j]
				s[j]=s[j+1]
				s[j+1]=temp
				temp=activity[j]
				activity[j]=activity[j+1]
				activity[j+1]=temp

def select():
	index=0
	print(activity[index])
	for i in range(1,n):
		if(s[i]>=f[index]):
			print(activity[i])
			index=i

s=[]
f=[]
n=int(input("enter the no. of activity:"))
activity=[i+1 for i in range(n)]
print("Enter their value:")
for i in range(n):
	s.append(int(input("si=")))
	f.append(int(input("si=")))
print("value are:")
print("activity",activity)
print("si=",s)
print("si=",f)
sorting()
print("after sorting:")
print("value are:")
print("activity",activity)
print("si=",s)
print("si=",f)
select()


