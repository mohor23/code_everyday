 #include <stdio.h>
void swap(int *a,int *b)
{
    int temp;
    temp=*a;
    *a=*b;
    *b=temp;
}
int partition(int arr[],int l, int h)
{
    int pivot=arr[l];
    int i=l;
    int j=h+1;
    while(i<j)
    {
        do
        {
            i++;
        }while(arr[i]<=pivot);
        do
        {
            j--;
        }while(arr[j]>pivot);
        if(i<j)
        {
            swap(&arr[i],&arr[j]);
        }
    }
     arr[l]=arr[j];
     arr[j]=pivot;
    return j;
}
void quick_sort(int arr[],int l,int h)
{   int j;
    if(l<h)
    {
        j=partition(arr,l,h);
        quick_sort(arr,l,j-1);
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
    for (i=0;i<n;i++) 
        printf("%d ",arr[i]);
    return 0;
}
