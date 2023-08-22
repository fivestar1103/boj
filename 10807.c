#include <stdio.h>
int main(){
    int n, arr[101], v, ans = 0, i;
    scanf("%d", &n);
    for(i=1; i<=n; i++) scanf("%d", &arr[i]);
    scanf("%d", &v);
    for(i=1; i<=n; i++) if(arr[i] == v) ans++;
    printf("%d", ans);
}