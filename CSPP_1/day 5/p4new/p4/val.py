val = input()
length = len(val)
for i in range(0,length,1):
	if i%2 ==0:
		print(val[i].upper(), end="")
	else:
		print(val[i].lower(), end="")
		