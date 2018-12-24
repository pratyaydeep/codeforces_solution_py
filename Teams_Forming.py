n=int(input())
a=list(map(int,input().split()))
a.sort()
sum=0
for i in range(0,n,2):
	sum+=(a[i+1]-a[i])
print(sum)
