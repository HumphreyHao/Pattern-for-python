def non_repeat_substring(str):
    #slide window
    left,right =0,0
    win_set = {}
    res_size =0
    #key =char, value = index
    #delete all the char between left and the meet
    for right in range(len(str)):
        win_right = str[right]
        if win_right in win_set:
            #we do not need to delete, just check left and the meet which one is bigger
            left = max(left,win_set[win_right])
        win_set[win_right] = right
        res_size = max(right-left+1,res_size)
    return res_size
