def remove_duplicates(arr):
    #two pointers
    #delete next,not the past
    left=0
    while 1:
        if left+1==len(arr):
            break
        else:
            if arr[left+1] == arr[left]:
                arr.pop(left+1)
            else:
                left+=1
    return len(arr)
            
