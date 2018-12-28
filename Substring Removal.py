danger=998244353  #as  I was not dividing by this number i got my solution wrong that is why i named it danger
n=int(input())
s=list(input())
if len(s)==2:
	print(3)
else:
	fs=s[0] #first string
	ls=s[-1] #last string
	fso=0 #number of times the first string repeated,until another string then (fs) is found
	lso=0 #number of times the last string repeated,until another string then (ls) is found
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
