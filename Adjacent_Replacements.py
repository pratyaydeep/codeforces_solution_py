n = input()
array = list(map(int,input().split()))
res=[str(x-1) if x%2==0 else str(x) for x in array]
print(' '.join(res))
