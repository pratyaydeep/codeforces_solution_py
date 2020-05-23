# Problem Link -> https://codeforces.com/problemset/problem/118/E
#Problem Statement :
'''
Bertown has n junctions and m bidirectional roads. We know that one can get from any junction to any other one by the existing roads.
As there were more and more cars in the city, traffic jams started to pose real problems. To deal with them the government decided to make the traffic one-directional on all the roads, thus easing down the traffic. Your task is to determine whether there is a way to make the traffic one-directional so that there still is the possibility to get from any junction to any other one. If the answer is positive, you should also find one of the possible ways to orient the roads.

The first line contains two space-separated integers n and m which represent the number of junctions and the roads in the town correspondingly. Then follow m lines, each containing two numbers which describe the roads in the city. Each road is determined by two integers a and b the numbers of junctions it connects.
It is guaranteed that one can get from any junction to any other one along the existing bidirectional roads. Each road connects different junctions, there is no more than one road between each pair of junctions.
If there's no solution, print the single number 0. Otherwise, print m lines each containing two integers p and q — each road's orientation.
'''

#Solution:

'''
Let's picture the problem as a Graph problem. The construction is only possible when all nodes of the graph is a part of a cycle. Only then we will have 2 or more paths to travel to a specific node.
If all nodes are part of a cycle, then there will be a back-edge(in the DFS traversal) for every node leading to any of it's ancestor node, so we can direct the traffic.
To check this we only need to check if there is a Bridge(Cut Edge) present in the graph.
'''

#Code ->

from sys import stdin,stdout,setrecursionlimit
from collections import  defaultdict
from threading import stack_size,Thread
setrecursionlimit(10**6)
stack_size(2**25)
adj=defaultdict(list)
visited=[False]*(100001)
intime=[0]*(100001)
outtime=[0]*(100001)
res=[]
bridge=False
timer=0
def dfs(node,par):
    global adj, visited, intime, outtime, res, bridge,timer
    visited[node]=True
    intime[node]=timer
    outtime[node]=timer
    timer+=1
    for j in adj[node]:
        if j==par:
            continue
        if visited[j]:
            outtime[node]=min(outtime[node],intime[j])
            if intime[node]>intime[j]:
                res.append((node,j))
        else:
            dfs(j,node)
            if outtime[j]>intime[node]:
                bridge=True
                return

            res.append((node,j))
            outtime[node] = min(outtime[node], outtime[j])



def solve():
    n,m=map(int,stdin.readline().split())
    global adj,visited,intime,outtime,res,bridge,timer
    timer=0
    bridge=False
    for i in range(m):
        u,v=map(int,stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    dfs(1,-1)
    if bridge:
        print(0)
    else:
        for i in range(len(res)):
            print(*res[i])

if __name__=='__main__':
	#solve()
	Thread(target=solve).start()
