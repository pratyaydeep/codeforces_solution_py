n=int(input())
a=list(map(int,input().split()))
if n==2:
	print(0)
else:
	a.sort()
	b=[]
	c=[]
	b=a[:n-1]
	c=a[1:n]
	val1=max(b)-min(b)
	val2=max(c)-min(c)
	if val1>=val2:
		print(val2)
	else:
		print(val1)
