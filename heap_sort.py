def heapify(arr,n,i):
    largest=i 
    l = 2*i+1     
    r = 2*i+2      
    if l<n and arr[i]<arr[l]: 
        largest=l 
    if r<n and arr[largest]<arr[r]: 
        largest=r 
    if largest!=i: 
        arr[i],arr[largest]=arr[largest],arr[i] 
        heapify(arr, n, largest) 
def heapsort(arr,n):  
    for i in range(n//2 - 1, -1, -1): 
        heapify(arr, n, i) 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0]=arr[0], arr[i]
        heapify(arr, i, 0) 
arr=[]
n=int(input("enter the number of elements of array"))
for i in range(0,n):
    ele=int(input("enter the elements of the array "))
    arr.append(ele)
print(arr)
heapsort(arr,n)
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i])
