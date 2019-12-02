#give the window, find the most frequency char
#if most+K > right -left+1, right++
#else, left++
def length_of_longest_substring(str, k):
    left,right =0,0
    win_set = {}
    res_size =0
    win_max = 0
    max_length=0
    for right in range(len(str)):
        win_right = str[right]
        if win_right in win_set:
            win_set[win_right]+=1
        else:
            win_set[win_right]=1
        win_max = max(win_max,win_set[win_right])
        if win_max+k>=right-left+1:
            continue
        else:
            #only the useful str we need to care
            #so the window will not shrink
            win_set[str[left]]-=1
            left+=1
        max_length = max(max_length, right - left + 1)
    return max_length

        