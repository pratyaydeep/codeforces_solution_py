for _ in range(int(input())):
	given=input().split()
	res=[]
	for i in given:
		res.append(i[1:]+i[0].lower()+'ay')
	temp=res[0]
	res[0]=temp[0].upper()+temp[1:]
	print(' '.join(res))
