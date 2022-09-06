# repeatedly switches adjacent items
# until there's none left to switch 
def bubbleSort(ar):
    s = len(ar)
    for i in range(s):
        done = True
        for j in range(s - i - 1):
            if ar[j] > ar[j+1]:
                ar[j],ar[j+1]=ar[j+1],ar[j]
                done = False
        if done == True:
            break

ar =[100,-2,50,-6,67,-80]
bubbleSort(ar)
print(ar)
