#source code for n queens
def abs(a):
	if(a>=0):
		return a
	else:
		return -a

def place(k,i):
	global arr
	for j in range(1,k):
		if arr[j]==i or abs(arr[j]-i)== abs(j-k):
			return False
	return True

def nqueen(k,n):
	global arr
	for i in range(1,n+1):
		if(place(k,i)):
			arr[k]=i
			if(k==n):
				temp=[]
				for p in range(n+1):
					temp2=[]
					for q in range(n+1):
						temp2.append('.')
					temp.append(temp2)
				for p in range(1,len(arr)):
					temp[p][arr[p]]='Q'
				for p in range(1,n+1):
					for q in range(1,n+1):
						print(temp[p][q],end=' ')
					print(' ')
				print('\n')
			else:
				nqueen(k+1,n)

n=int(input("Enter the no of queens:"))
arr=[]
q=[]
for i in range(0,n+1):
	arr.append('0')
print('possible place or solution are:')
nqueen(1,n)
