def selectSort(arr):
    if len(arr) < 2:
        return
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                (arr[i],arr[j])=(arr[j],arr[i])
                
arr =[100,-5,22,7,-100]
selectSort(arr)
print(arr)
