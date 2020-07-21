//Given an unsorted array of nonnegative integers, find a continuous subarray which adds to a given number
#include <stdio.h>
int subarray_sum(int arr[],int n,int sum)
{
   int i;
   int curr_sum=arr[0];
   int start=0;
   for(i=1;i<n;i++)
   {
      while(curr_sum>sum && start<i-1)
      {
          curr_sum=curr_sum-arr[start];
          start++;
      }
      if(curr_sum==sum)
      {
          printf("the sum of the array is between %d and %d",start,i-1);
          return 1;
      }
      if(i<n)
      {
          curr_sum=curr_sum+arr[i];
      }
   }
   printf("subarray not found");
   return 0;
}

int main()
{
    int n,i,sum;
    int arr[100];
    printf("enter the size of array");
    scanf("%d",&n);
    printf("enter the array");
    for(i=0;i<n;i++)
    {
      scanf("%d",&arr[i]);  
    }
    printf("enter the sum:");
    
    scanf("%d",&sum);
    subarray_sum(arr,n,sum);
    

    return 0;
}
