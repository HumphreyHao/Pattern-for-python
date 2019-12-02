def make_squares(arr):
    #sorted-two pointers
    #if arr[right] > arr[left],arr[right]--
    #arr[left] >arr[right],arr[left]++
    left,right =0,len(arr)-1
    res=[]
    while left<=right:
        if arr[right]*arr[right]>=arr[left]*arr[left]:
            res.append(arr[right]*arr[right])
            right-=1
        else:
            res.append(arr[left]*arr[left])
            left+=1
    res.reverse()
    return res
print(make_squares([-2, -1, 0, 2, 3]))
