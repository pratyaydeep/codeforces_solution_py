/*
Problem Statement :
Diameter of a tree is defeined as the longest path between any two nodes in the tree(Undirected).
You are given a tree find it's diameter

Novice Solution:
We would run DFS for each node. In each iteration we would take the i'th node as root and find the farthest node.
The maximum of all this will be our solution.

Better Solution:
We can find Diameter in only two DFS traversals.
Take any arbitrary node as root and run DFS from it and find the farthest node, let this be X.
Run a DFS from X and find the maximum distance from this node to any other node, this distance is the Diameter.
*/

//Solution Code:
#include<bits/stdc++.h>
using namespace std;
vector<int> ar[10001]; int vis[10001], maxD, X;
void dfs(int node, int d){
	vis[node]=1;
	if (d>maxD) maxD=d, X=node;
	for (int child: ar[node])
		if (vis[child]==0) dfs(child,d+1);
}
int main(){
	int n,a,b;
	cout<<"Enter number of nodes :";
	cin>>n;
	for(int i=1; i<n; i++){
		cout<<"\nEnter any two nodes which are connected :";
		cin>>a>>b, ar[b].push_back(a), ar[a].push_back(b);
	}
	maxD=-1;
	dfs(1,0);
	for(int i=0; i<=n; i++) vis[i]=0;
	maxD=-1;
	dfs(X,0);
	cout<<"\nThe Diameter is :"<<maxD<<endl;
}