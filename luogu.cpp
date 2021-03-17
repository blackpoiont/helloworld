#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>


#define MOD 1000000007

using namespace std;

int n, m;
int b[35][35];
int ans[35][35];

void b_b()
{
    int tmp[35][35];
    memset(tmp, 0, sizeof(tmp));

    for(int i=1; i<=n; i++)
    {
        for(int j=1; j<=n; j++)
        {
            for(int k=1; k<=n; k++)
            {
                tmp[i][j] = (tmp[i][j] + b[i][k]*b[k][j]);
            }
        }
    }

    for(int i=1; i<=n; i++)
    {
        for(int j=1; j<=n; j++)
        {
            b[i][j] = tmp[i][j];
        }
    }
}

void ans_b()
{
    int tmp[35][35];
    memset(tmp, 0, sizeof(tmp));

    for(int i=1; i<=n; i++)
    {
        for(int j=1; j<=n; j++)
        {
            for(int k=1; k<=n; k++)
            {
                tmp[i][j] = (tmp[i][j] + ans[i][k]*b[k][j]);
            }
        }
    }

    for(int i=1; i<=n; i++)
    {
        for(int j=1; j<=n; j++)
        {
            ans[i][j] = tmp[i][j];
        }
    }
}

void work()
{
    while(m)
    {
        if(m&1)
        {
            ans_b();
        }

        b_b();
        m >>= 1;

    }
}

void solve()
{
    for(int i=1; i<=n; i++)
    {
        ans[i][i] = 1;
    }

    cin >> n >> m;
    for(int i=1; i<=n; i++)
    {
        for(int j=1; j<=n; j++)
        {
            cin >> b[i][j];
        }
    }

    work();

    for(int i=1; i<=n; i++)
    {
        for(int j=1; j<=n; j++)
        {
            cout << ans[i][j] << ' ';
        }
        cout << endl;
    }
}

int main(void)
{
    
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    // come on
    solve();

    return 0;
}
