cube=27
ep=0.01
guess=0.0
increament=0.0001
num_guess=0
while abs(guess**3-cube)>=ep:
	guess+=increament
	num_guess+=1
	print("num_guess=",num_guess)
	if abs(guess**3-cube)>=ep:
		print("failed on cube root of :",cube)
	else:
		print("failed on cube root of :",cube)
