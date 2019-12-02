def pair_with_targetsum(arr, target_sum):
    #two pointers
    left,right =0,len(arr)-1
    while left<right:
        tmp = arr[left]+arr[right]
        if tmp<target_sum:
            left+=1
        elif tmp>target_sum:
            right-=1
        else:
            return [left,right]
    return [0,0]

