#include <stdio.h>
int main(){
    int ans[3] = {-1}, tmp, i, j;
    for(i=1;i<=9;i++) for(j=1;j<=9;j++){
        scanf("%d", &tmp);
        if(tmp>ans[0]){
            ans[0] = tmp;
            ans[1] = i;
            ans[2] = j;
        }
    }
    printf("%d\n%d %d", ans[0], ans[1], ans[2]);
}