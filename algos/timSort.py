"""
split into 'runs' of almost sorted 
chunks
insertion_sort the chunks
the merge_sort the chunks

Still has bugs
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
    runs = []
    arun = [ar[0]]
    i = 1
    while i < len(ar):
        if ar[i] < ar[i-1]:
            runs.append(arun)
            arun = [ar[i]]
        else:
            arun.append(ar[i])
            
        i+=1
    runs.append(arun)
    
    sortedRuns = []
    sortedAr = []
    for run in runs:
        sortedRuns.append(insertion_sort(run))
    for run in sortedRuns:
        sortedAr = merge(sortedAr,run)
    return sortedAr

    
    
ar=[43,55,2,6,7,65,3,2,8,77,78,4,39,40,41,1,67]

#insertion_sort(ar)
ar = tim_sort(ar)
print(ar)





