# merge sort, recursively split to
# units then merge back up
def merge(ar1, ar2):
    if len(ar1)==0:
        return ar2
    if len(ar2)==0:
        return ar1
    
    res = []
    xar1 = xar2 = 0
    
    while len(res) < len(ar1) + len(ar2):
        if ar1[xar1] <= ar2[xar2]:
            res.append(ar1[xar1])
            xar1+=1
        else:
            res.append(ar2[xar2])
            xar2+=1
            
        if xar1 == len(ar1):
            res+=ar2[xar2:]
            break
        if xar2 == len(ar2):
            res+=ar1[xar1:]
        
    return res
    
def sortMerge(ar):
    if len(ar) < 2:
        return ar

    mid = len(ar) // 2
    
    return merge(
        sortMerge(ar[:mid]),
        sortMerge(ar[mid:]))
        
ar = [3,2,1,0,-4,55,-66,8,9]
ar = sortMerge(ar)
print(ar)
