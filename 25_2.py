#winset to count the 1 numbers
#if winsize - 1 number < k, right++
#left++(the whole window move, because we only need the longest one)
def length_of_longest_substring(arr, k):
    left,right =0,0
    win_set={}
    win_set[1]=0
    win_set[0]=0
    res_size =0
    for right in range(len(arr)):
        win_right = arr[right]
        if win_right ==1:
            win_set[1]+=1
        else:
            win_set[0]+=1
        if right-left+1>win_set[1]+k:
            if arr[left] == 1:
                win_set[1]-=1
            else:
                win_set[0]-=1
            left+=1
        res_size = max(res_size,right-left+1)
    return res_size