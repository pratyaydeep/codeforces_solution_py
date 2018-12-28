n=int(input())
s=list(input())
res=[]
i=1
if n==1:
	print(*s)
else:
	while len(s)>1:
		res=res+[(s[0])]

		del(s[:i])
		i=i+1
	print(''.join(res))
