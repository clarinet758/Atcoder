#include<bits/stdc++.h>
using namespace std;

int main(){
    int m,ans;
    scanf("%d",&m);
    if (m<100) ans=0;
    else if (m<=5000) ans=m/100;
    else if (m<=30000) ans=m/1000+50;
    else if (m<=70000) ans=(m-30000)/5000+80;
    else ans=89;
    printf("%02d\n",ans);
    return 0;
}
