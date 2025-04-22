def selectionSort(arr,num):
    for i in range(num):
        min=i
        for j in range(i+1,num):
            if arr[j]<arr[min]:
                min=j
        (arr[i],arr[min])=(arr[min],arr[i])

num=int(input("Enter the no:"))
arr=list(map(int,input ("Enter the numbers:").strip().split()))[:num]
selectionSort(arr, num)
print("The array after sorting:", arr)