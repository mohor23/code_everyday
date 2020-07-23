//Given an array of integers you have to find three numbers such that sum of two elements equals the third element.
def triplet(arr,n):
    arr.sort()
    i=n-1
    count=0
    while(i>=0):
        j=0
        k=i-1
        if(arr[i]==arr[j]+arr[k]):
            print("the triplets are:",arr[j],arr[k],arr[i])
            count+=1
        elif (arr[i] > arr[j] + arr[k]): 
                j += 1
        else: 
                k -= 1
        i -= 1
    print ("No such triplet exists")
    print(count)
n=int(input("enter the number of elements"))
arr=[]
for i in range(0,n):
    ele=int(input('enter the elements'))
    arr.append(ele)
print(arr)
triplet(arr,n)
