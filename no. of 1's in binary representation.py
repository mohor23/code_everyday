//3.Find the number of 1 in binary representation of number
//example-[5]=>>>>>Ans is 2
arr=[]
n=int(input("enter the number in decimal form"))
while(n!=0):
    ele=n%2
    arr.append(ele)
    n=n//2
print(arr)
count=0
for i in range(0,len(arr)):
    if(arr[i]==1):
        count=count+1
print(count)
