T = int(input())
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for t in range(T):
	l=[]
	s=[]
	n,k=map(int,input().split())
	for i in range(k):
		l.append(alpha[i])
	l=l*(n//k)
	s=l
	for i in range(n%k):
		s.append(alpha[i])
	print(*s,sep='',end='\n')
