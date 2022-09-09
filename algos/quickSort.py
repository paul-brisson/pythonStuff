# switch around a pivot, split at the
# pivot, recurse on the sub-arrays
def switcher(ar,bot,top):
    piv = ar[(bot + top) // 2]
    
    i = bot-1
    j = top+1
    
    while True:
        i+=1
        while ar[i] < piv:
            i+=1
        
        j-=1    
        while ar[j] > piv:
            j-=1
            
        if i>=j:
            return j

        ar[i],ar[j]=ar[j],ar[i]
            
def rquick_sort(arr,bot,top):
    if bot < top:
        splt = switcher(ar,bot,top)
        rquick_sort(ar,bot,splt)
        rquick_sort(ar,splt+1,top)

def quick_sort(ar):
    if len(ar) < 2:
        return

    (ar,0,len(ar)-1)

ar=[55,8,77,-1,88,5,4,89,33,52,-100]
quick_sort(ar)
print(ar)
