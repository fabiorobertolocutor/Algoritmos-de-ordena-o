# https://www.youtube.com/watch?v=qzXAVXddcPU&ab_channel=RunTimeClips

def shellSort(arr, n):
    gap=n//2
     
    while gap>0:
        j=gap
    
        while j<n:
            i=j-gap 
             
            while i>=0:
                if arr[i+gap]>arr[i]:
                    break
                else:
                    arr[i+gap],arr[i]=arr[i],arr[i+gap]
                i=i-gap 
           
            j+=1
        gap=gap//2

input = [5,4,3,2,1]
shellSort(input, len(input))
print(input)