#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define PI 3.1415926535897932

long long dp[105][2][5];
int main(){
    int k,x;
    char n[105];
    scanf("%s",n);
    sc1(k);
    dp[0][0][0]=1;
    x=strlen(n);
    for (int i=1;i<=x;i++) {
        for (int j=0;j<4;j++) {
            if (dp[i-1][0][j]>0) {
                if (n[i-1]-'0'>0) dp[i][0][j+1]=1;
                else dp[i][0][j]=1;
                for (int m=0;m<n[i-1]-'0';m++) {
                    if (m==0) dp[i][1][j]+=1;
                    else dp[i][1][j+1]+=1;
                }
            }
            if (dp[i-1][1][j]>0) {
                dp[i][1][j+1]+=dp[i-1][1][j]*9;
                dp[i][1][j]  +=dp[i-1][1][j];
            }
        }
    }
    printf("%lld\n",dp[x][0][k]+dp[x][1][k]);
    return 0;
}
