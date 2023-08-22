#include <stdio.h>
int main(){
    int n, m, arr[101][101], tmp, i, j;
    scanf("%d%d", &n, &m);
    for(i=1;i<=n;i++) for(j=1;j<=m;j++) scanf("%d", &arr[i][j]);
    for(i=1;i<=n;i++){
        for(j=1;j<=m;j++){
            scanf("%d", &tmp);
            printf("%d ", arr[i][j] + tmp);
        }
        printf("\n");
    }
}