'''algorithm to find all 1d peak in an unsorted list if one exists.'''

l = [1,4,7,0,2,4,7,9,6,4,3,0,1,4,7,4,2,9]

def peakfind(l):
    for i in l:
        if (l[i] > l[i-1]) and (l[i] > l[i+1]): 
                return "peak is {}".format(l[i])
                
print(peakfind(l)) 
