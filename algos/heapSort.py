# build max heap to extract
# the highest and then recurse on the 
# rest of the array
def max_heap(ar,size,startx):
    largest = startx
    leftx = (startx*2)+1
    rigtx = (startx*2)+2
    
    if leftx < size and ar[leftx] > ar[largest]:
        largest = leftx

    if rigtx < size and ar[rigtx] > ar[largest]:
        largest = rigtx

    if largest != startx:
        ar[startx],ar[largest] = ar[largest],ar[startx]
        max_heap(ar,size,largest)
    
def heap_sort(ar):
    
    size = len(ar)
        
    for i in range(size,-1,-1):
        max_heap(ar,size,i)
         
    for i in range(size -1,0,-1):
        ar[0],ar[i]=ar[i],ar[0]
        max_heap(ar,i,0)
         
         
ar=[22,19,7,33,8,44,24,-1,16,50,5,4,3,11,-100]
heap_sort(ar)
print(ar)
