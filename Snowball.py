current_weight,s=map(int,input().split())
ws1,hs1=map(int,input().split())
ws2,hs2=map(int,input().split())
stones={}
stones[hs1]=ws1
stones[hs2]=ws2
for current_height in range(s,0,-1):
	current_weight+=current_height
	if current_height in stones:
		current_weight-=stones[current_height]
		if current_weight<0:
			current_weight=0
print(current_weight)
