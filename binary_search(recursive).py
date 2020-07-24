//binary search using recursion in python
def binary_search(arr,l,h,number):
    if l<=h:
        mid=(l+h)//2
        if(arr[mid]==number):
            return mid
        elif(number<arr[mid]):
            binary_search(arr,l,mid-1,number)
        else:
            binary_search(arr,mid+1,h,number)
    else:
        return -1
arr=[]
n=int(input("enter the number of elements of array"))
for i in range(0,n):
    ele=int(input("enter the elements of the array in sorted order"))
    arr.append(ele)
print(arr)
number=int(input("enter the element to be searched"))
result=binary_search(arr,0,n-1,number)
if(result==-1):
    print("element not found")
else:
    print("element found at index",result)
