#first to find the max length which contains the whole pattern
#then try to shrink, when the right == left,left++, until one character fre =0
#left-=1, then use this window to tranverse again
def find_substring(str, pattern):
    right,left =0,0
    win_dict = {}
    pattern_set = []
    res_size=len(str)
    res=''
    for i in pattern:
        if i not in pattern_set:
            pattern_set.append(i)
    for right in range(len(str)):
        win_right = str[right]
        if win_right in win_dict:
            win_dict[win_right]+=1
        else:
            win_dict[win_right]=1
        if right<len(pattern_set):
            continue
        if len(win_dict)<len(pattern_set):
            continue
        flag=0
        for i in pattern_set:
            if i not in win_dict:
                flag=1
                break
        if flag ==1:
            continue
        while left<right:
            if str[left] not in pattern_set:
                left+=1
            else:
                if win_dict[str[left]]-1>0:
                    win_dict[str[left]]-=1
                    left+=1
                else:
                    break
        if res_size> right-left+1:
            res_size=right-left+1
            res=str[left:right+1]
    return res
find_substring('aabdec', 'abc')


        
        