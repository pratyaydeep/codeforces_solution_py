for _ in range(int(input())):
	l,r=map(int,input().split())
	_pp=range(l,r+1)
	for i in _pp:
		if i*2 in _pp:
			print(i,i*2)
			break
