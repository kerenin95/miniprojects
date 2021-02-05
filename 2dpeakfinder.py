'''algorithm to find a peak in a 2d array if one exists'''

arr = [[1,4,2,3],[8,6,0,7],[4,7,5,8],[2,5,1,0]]

def peakfinder2(arr):
    for i in len(arr):
        if (arr[i] > arr[i+1]) and (arr[i] > arr[i-1]):
            
            for j in arr[i]:
                if (arr[i[j]] > arr[i[j+1]]) and (arr[i[j]] > arr[i[j-1]]):
                    return "peak is {}{}".format(arr[i], arr[i[j]])

print(peakfinder2(arr))