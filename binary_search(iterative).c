//binary search using iterative methord using c
#include <stdio.h>
int binary_search(int arr[],int n,int ele)
{
    int l=0;
    int h=n-1;
    int mid;
    while(l<=h)
    {
        mid=(l+h)/2;
        if(arr[mid]==ele)
        {
            return mid;
        }
        else if(ele<arr[mid])
        {
            h=mid-1;
        }
        else 
        {
            l=mid+1;
        }
    }
    return -1;
}
int main()
{ 
    int n,i;
    int ele;
    int ans;
    int arr[100];
    printf("enter the number of elements in array");
    scanf("%d",&n);
    printf("enter the elements in sorted order");
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    printf("enter the element to be searched");
    scanf("%d",&ele);
    ans=binary_search(arr,n,ele);
    if(ans==-1)
    {
        printf("element not found");
    }
    else
    {
        printf("element found at index %d",ans);
    }

    return 0;
}
