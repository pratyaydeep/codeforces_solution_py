import sys
a=[]
sum=0
height=int(input())
s=int(input())
sum+=s
a.append(s)
a.append(s*(-1))
for _ in range(height-1):
	inp=int(input())
	sum+=inp
	temp=[]
	for i in a:
		temp.append(i+inp)
		temp.append(i-inp)
	a=temp[:]
if 0 in a:
	print('YES')
else:
	for i in a:
		if i%360==0:
			print('YES')
			sys.exit()
	print('NO')
