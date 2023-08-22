#include <stdio.h>
int main(){
    int n, arr[101][101], x, y, i, j, k, ans = 0;
    for(i=0;i<=100;i++) for(j=0;j<=100;j++) arr[i][j] = 0;
    scanf("%d", &n);
    for(i=0;i<n;i++){
        scanf("%d%d", &x, &y);
        for(j=y+1;j<=y+10;j++) for(k=x+1;k<=x+10;k++) arr[j][k] = 1;
    }
    for(i=0;i<=100;i++) for(j=0;j<=100;j++) if(arr[i][j]) ans++;
    printf("%d", ans);
}