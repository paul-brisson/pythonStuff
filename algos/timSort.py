"""
split into 'runs' of almost sorted 
chunks
insertion_sort the chunks
the merge_sort the chunks
"""

def insertion_sort(ar):
    for i in range(1,len(ar)):
        value = ar[i]
        j=i-1
        while j >= 0 and ar[j]>value:
            ar[j+1]=ar[j]
            j-=1
        ar[j+1]=value
        
"""
this is not a merge sort.
it only merges but expects arguments
are already sorted asc
"""
def merge(ar, run):
    if not ar:
        return run
    if not run:
        return ar

    if ar[0]<=run[0]:
        return [ar[0]] + merge(ar[1:],run)
    return [run[0]] + merge(ar+run[1:])
    
def tim_sort(ar):
    print("todo")
    
ar=[43,55,2,6,7,65,3,2,8,77,78,4,39,40,41,1,67]

#insertion_sort(ar)
tim_sort(ar)
print(ar)

