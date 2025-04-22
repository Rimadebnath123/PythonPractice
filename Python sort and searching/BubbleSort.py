def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if(array[j])>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp

num=int(input("Enter the number:"))
data = list(map(int, input("Enter the numbers: ").strip().split()))[:num]
print("list is-",data)
bubbleSort(data)
print("sorted array is assending order:",(data))
