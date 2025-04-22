def binary_Search(arr,n):
    low=0
    high=len(arr)-1
    mid=0
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<n:
            low=mid+1
        elif arr[mid]>n:
            high=mid-1

        else:
            return mid
    return -1
    
num=int(input("Enter the no:"))
arr=list(map(int, input("Enter the numbers :").strip().split()))[:num]
n=int(input("Enter the key:"))
result=binary_Search(arr,n)

if(result!=-1):
    print("element is present at index",str(result))
else:
    print("element is not present in array")