#a change type slide window, with only two kinds of things
def fruits_into_baskets(fruits):
    left,right =0,0
    win_dict = {}
    res_max =0
    for right in range(len(fruits)):
        if fruits[right] in win_dict:
            win_dict[fruits[right]]+=1
        else:
            win_dict[fruits[right]]=1
        #check kinds
        while(len(win_dict)>2):
            win_dict[fruits[left]]-=1
            if win_dict[fruits[left]] == 0:
                del win_dict[fruits[left]]
            left+=1
        res_max = max(res_max,right-left+1)
    return res_max
