t=list(input())
o=[]

if len(t)%2==0:
	while len(t)>0:
		o.append(t[-1])
		del(t[-1])
		o.append(t[0])
		del(t[0])
	o.reverse()
	print(''.join(o))
else:
	while len(t)>1:
		o.append(t[0])
		del(t[0])
		o.append(t[-1])
		del(t[-1])
	o=o+t
	o.reverse()
	print(''.join(o))
