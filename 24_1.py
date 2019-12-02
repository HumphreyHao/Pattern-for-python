def longest_substring_with_k_distinct(str, k):
    #use a win_set to save the win's elements
    #update its length
    #return length
    win_set={}
    left=0
    right=0
    win_maxsize=0
    for right in range(len(str)):
        if str[right] in win_set:
            win_set[str[right]]+=1
        else:
            win_set[str[right]]=1
        #check i
        while(len(win_set)>k):
            win_set[str[left]]-=1
            if win_set[str[left]] == 0:
                del win_set[str[left]]
            left+=1
        win_maxsize = max(right-left+1,win_maxsize)
    return win_maxsize
print (longest_substring_with_k_distinct("arraci",2))    