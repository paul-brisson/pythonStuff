# this one pushes any left greater than
# ar[i] up to the right
def insertionSort(ar):
    s = len(ar)
    for i in range(1,s):
        down = ar[i]
        j = i-1
        while j >= 0 and ar[j] > down:
            ar[j+1]=ar[j]
            j-=1
            print(ar)
            
        ar[j+1]=down
        print(ar)

ar=[3,2,1,4,5,6,9,8,7]
insertionSort(ar)
print(ar)
