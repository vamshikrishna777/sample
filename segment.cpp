#include<bits/stdc++.h>
#include<vector>
#include<iterator>
using namespace std;
int main()
{
    // cout<<"This is fake segment tree\n";
    vector<int> v;
    for(int i=5;i>=0;i--) v.push_back(i);
    for(int i=0;i<5;i++) cout<<v[i]<<" ";
    cout<<endl;
    for(auto i:v) cout<<i+6<<"\n";
    sort(v.begin(),v.end());
    for(auto i:v) cout<<i<<" ";
    return 0;
}