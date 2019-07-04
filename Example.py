a="asdfghjklPOIUYTREWQ"
word=input("Enter your words:")
times=int(input("Enthusim level(1-10):"))
i=0
while i<len(word):
	char=word[i]
	if char in a:
		print("give me cheerr:"+char+"!"+char)
	else:
		print("give me cheerr:"+char+"!"+char)
	i+=1
print("what does spell:")
for i in range (times):
	print(word,"!!!")
