//to check if a given number is a power of 2 ?
#include <stdio.h>

int main()
{
    int n;
    printf("enter the number");
    scanf("%d",&n);
    if((n & (n-1))==0)
    {
        printf("the number is power of 2");
    }
    else
    {
        printf("the number is not a power of 2");
    }

    return 0;
}
