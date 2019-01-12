card=input()
cards=input().split()
s=False
for c in cards:
	if c[0] in card:
		s=True
		break
	if c[1] in card:
		s=True
		break
if s:
	print('YES')
else:
	print('NO')
