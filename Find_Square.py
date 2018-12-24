n,m=map(int,input().split())
data=[]
blacklist=[]
middlelist=[]
for i in range(n):
    a=input()
    data.append(a)
    if 'B' in a:
        blacklist.append(i)
mr=blacklist[int(((len(blacklist)+1)/2))-1]
for j in range(len(data[mr])):
    if data[mr][j]=='B':
        middlelist.append(j)
print(str(blacklist[(int((len(blacklist)+1)/2))-1]+1) + ' ' + str(middlelist[int(((len(middlelist)+1)/2))-1]+1))
