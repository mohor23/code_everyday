//1.Find number of rotations in a circularly sorted array
//example-1.[4,6,2,3] =>>>>>> Ans is 2.
def rotations(arr,n):
    minimum=arr[0]
    min_index=0
    for i in range(1,n):
         if(minimum>arr[i]):
            minimum=arr[i]
            min_index=i
            count=n-i
            return count
arr=[]
n=int(input("Enter the size of the array:"))
print("Enter the elements:",end="")
for i in range(0,n):
    ele=int(input())
    arr.append(ele)
result=rotations(arr,n)
print("The count is:",result)
