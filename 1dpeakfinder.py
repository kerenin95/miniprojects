'''algorithm to find all 1d peak in an unsorted list if one exists.'''

l = [1,4,7,0,2,4,7,9,8,4,7,9,1,4,7,4,2,9]

def peakfind(l):
    midpoint = (len(l) // 2) # find the midpoint value
    
    if l[midpoint] < l[midpoint + 1]: # if the right side is greater scan the right side for a peak
        for i in l[midpoint: -1]: 
            if l[i] > l[i+1]: # compare current value with neighbors on right side
                return "the peak on the right is {}".format(l[i])
    
    elif l[midpoint] < l[midpoint - 1]: # if the left side of the midpoint is greater 
        for j in l[0: midpoint]: # scan the left side of midpoint for a peak
            if l[j] > l[j-1]: # compare current value with item on the left
                return "the peak on the left is {}".format(l[j])
    
    else: # if the midpoint is a peak already
        return "the peak is middle value({})".format(l[midpoint])        
                
print(peakfind(l)) 
