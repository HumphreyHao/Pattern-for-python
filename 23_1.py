def find_averages_of_subarrays(K, arr):
    #version2,not the arr but just cal the change
    res =[]
    #use this way we can only append, but not use index
    window_sum =0
    left,right=0,0
    for right in range(len(arr)):
        window_sum+=arr[right]
        if right< K-1:
            continue
        else:
            average = window_sum/K
            res.append(average)
            window_sum-=arr[left]
            left+=1
    return res




