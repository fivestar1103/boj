#include <stdio.h>

int main(){
    int arr[41], n, i;
    scanf("%d", &n);
    arr[1] = arr[2] = 1;
    for (i = 3; i <= n; i++) arr[i] = arr[i-1] + arr[i-2];
    printf("%d %d", arr[n], n-2);
    return 0;
}