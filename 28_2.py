def dutch_flag_sort(arr):
    #make 0 before left, and make 2 after right
    left,right =0,len(arr)-1
    i=0
    while i <= right:
        if arr[i]==0:
            arr[i],arr[left] = arr[left],arr[i]
            left+=1
            i+=1
        elif arr[i] ==1 :
            i+=1
        else:
            arr[i],arr[right] = arr[right],arr[i]
            right-=1
    return arr
