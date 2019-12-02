import math
def smallest_subarray_with_given_sum(s, arr):
    #if the win_sum is bigger than s, left++
    #else right++
    left,right=0,0
    win_sum=0
    res_size=len(arr)
    while right<len(arr):
        if arr[right]>s:
            return 1
        win_sum+=arr[right]
        #here we can insert a loop to shrink the array as we want
        while win_sum>=s:
            #here we will use python min to get
            res_size = min(res_size,right-left)
            win_sum-=arr[left]
            left+=1
        if res_size== math.inf:
            return 0
    return res_size
    
        

