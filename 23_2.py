def max_sub_array_of_size_k(k, arr):
    #save the index of the max subarr and update it
    maxindex =0
    maxvalue =0
    left,right=0,0
    win_sum=0
    for right in range(len(arr)):
        win_sum+=arr[right]
        if right>=k-1:
            if win_sum>maxvalue:
                maxvalue = win_sum
                maxindex=right
            win_sum-=arr[left]
            left+=1
    return maxvalue
