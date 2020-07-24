#include <stdio.h>
void swap(int *a,int *b)
{
    int temp;
    temp=*a;
    *a=*b;
    *b=temp;
}
partition(arr[],int l, int h)
{
    int pivot=l;
    int i=l;
    int j=h;
    while(i<j)
    {
        do
        {
            i++;
        }while(i<=pivot);
        do
        {
            j--;
        }while(j>pivot);
        if(i>j)
        {
            swap(arr[i],arr[j]);
        }
    }
    swap(arr[l],arr[j]);
    return j;
}
quick_sort(int arr[],int l,int h)
{   int j;
    if(l<h)
    {
        j=partition(arr,l,h);
        quick_sort(arr,l,j);
        quick_sort(arr,j+1,h);
    }
    
}
int main()
{
    int n,i;
    int arr[100];
    printf("enter the size of array");
    scanf("%d",&n);
    printf("enter the elements of the array");
    for(i=0;i<n;i++)
    {
      scanf("%d",&arr[i]);  
    }
    quick_sort(arr,0,n-1);
    return 0;
}
