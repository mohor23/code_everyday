//2.Find the smallest missing Number in a sorted array
//example-2.[0,1,2,6,9,11,15]=>>>>>Ans is 3
arr=[]
n=int(input("enter the number of elements"))
for i in range(0,n):
    ele=int(input("enter the elements in sorted order"))
    arr.append(ele)
index=0
for i in range(0,n):
    if(arr[i]==index):
        index=index+1
        if(i==n-1):
            print("the smallest missing value is",n)
        continue
    elif(arr[i]!=index):
        print("the smallest missing value is",index)
        break
    
