#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<int> temp;
vector<int> ans;

void dfs(int c, long long value, long long target)
{
    if(c == 1)
    {
        ans.push_back(temp[0]);
        return;
    }
    
    for(int i = 1; i <= c; i++)
    {
        long long sum_v = i * value;
        if(target <= sum_v)
        {
            sum_v = (i-1) * value;
            ans.push_back(temp[i-1]);
            temp.erase(temp.begin()+(i-1));
            dfs(c-1, value / (c - 1), target-sum_v);
            break;
        }
    }
    return;
}

vector<int> solution(int n, long long k) {
    for(int i = 1; i <= n; i++)
    {
        temp.push_back(i);
    }
    
    sort(temp.begin(), temp.end());
    
    long long a = 1;
    
    for(int i = 1; i <= n-1; i++)
    {
        a *= i;
    }
    
    dfs(n, a, k);
    
    return ans;
}