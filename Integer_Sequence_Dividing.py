n=int(input())
if n==1:
	print(1)
elif n==2:
	print(1)
elif n%2==1:
	noones=(n//2)+1
	if noones%2==0:
		print(0)
	else:
		print(1)
elif n%2==0:
	noones=(n//2)
	if noones%2==0:
		print(0)
	else:
		print(1)
