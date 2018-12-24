n=int(input())
voc = list(map(int,input().split()))
dup = []
for i in voc:
    dup.append(voc.count(i))
print(max(dup))
