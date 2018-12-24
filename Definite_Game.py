v=int(input())
if v==1:
	print(1)
if v==2:
	print(2)
else:
	for i in range(v):
		if v%(v-i)!=0:
			print(v%(v-i))
			break
