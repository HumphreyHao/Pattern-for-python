def find_subarrays(arr, target):
    #slide windows
    win_product = 1
    left,right =0,0
    res =[]
    for right in range(len(arr)-1):
        win_product *= arr[right]
        if win_product < target:
            #all the subarray will be added
            for i in range(0,right,1):
                tmp=arr[i:right+1]
                res.append(tmp)
            continue
        else:
            while win_product>target:
                win_product/=arr[left]
                left+=1
            for i in range(left,right,1):
                tmp=arr[i:right+1]
                res.append(tmp)
    return res


    