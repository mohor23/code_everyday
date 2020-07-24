//insertion sort in c
#include <stdio.h>
insertion_sort(int arr[],int n)
{
    
    int i,temp,j; 
    for (i = 1; i < n; i++) 
    { 
        temp=arr[i]; 
        j = i - 1; 
        while(j>= 0&&arr[j]>temp)
        { 
            arr[j+1]=arr[j]; 
            j=j-1; 
        } 
        arr[j+1]=temp; 
    }
    for (i = 0; i < n; i++) 
        printf("%d ", arr[i]);
}
int main()
{
    int n,i;
    int arr[100];
    printf("enter the size of array");
    scanf("%d",&n);
    printf("enter the array");
    for(i=0;i<n;i++)
    {
      scanf("%d",&arr[i]);  
    }
    insertion_sort(arr,n);
    return 0;
}
