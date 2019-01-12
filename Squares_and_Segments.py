from math import sqrt
def nearest_square(num):
	lhv=int(sqrt(num))**2
	rhv=(int(sqrt(num))+1)**2
	ld=num-lhv
	rd=rhv-num
	if rd>ld:
		return lhv
	else:
		return rhv

number=int(input())
if number==1:
	print(2)
elif number==2:
	print(3)
else:
	if number == int(sqrt(number))**2:
		print(int(sqrt(number))*2)
	elif number>nearest_square(number):
		print(int(sqrt(nearest_square(number)))*2 + 1)
	elif number<nearest_square(number):
		print(int(sqrt(nearest_square(number)))*2)
