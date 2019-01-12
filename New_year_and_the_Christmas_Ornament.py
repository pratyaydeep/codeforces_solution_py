y,b,r=map(int,input().split())
arr=[p+q+s for p in range(y+1) for q in range(b+1) for s in range(r+1) if q==p+1 and s==q+1]
print(max(arr))
