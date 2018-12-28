danger=998244353
n=int(input())
s=list(input())
if len(s)==2:
	print(3)
else:
	fs=s[0]
	ls=s[-1]
	fso=0
	lso=0
	for i in s:
		if i==fs:
			fso+=1
		else:
			break
	for i in s[::-1]:
		if i==ls:
			lso+=1
		else:
			break

	if fs==ls:
		ans=(fso+1)*(lso+1)
	else:
		ans=1+fso+lso
	print(ans%danger)
