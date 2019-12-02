#substring - slide window
#the size is constant, so just use slide window to count the frequency
#if equal,return true
def find_permutation(str, pattern):
    left,right = 0,0
    win_dict = {}
    pattern_dict={}
    for i in pattern:
        if i in pattern_dict:
            pattern_dict[i]+=1
        else:
            pattern_dict[i]=1
    for right in range(len(str)):
        win_right=str[right]
        if win_right not in pattern_dict:
            left =right+1
            win_dict.clear()
            continue
        if win_right in win_dict:
            win_dict[win_right]+=1
        else:
            win_dict[win_right]=1
        if right-left+1<len(pattern):
            continue
        if win_dict[win_right]<pattern_dict[win_right]:
            continue
        elif win_dict[win_right] >pattern_dict[win_right]:
            #shrink the window
            while win_dict[win_right] >pattern_dict[win_right]:
                win_dict[str[left]]-=1
                left+=1
        else:
            flag=0
            if len(win_dict) != len(pattern_dict):
                continue
            for x in win_dict:
                if  (win_dict[x] != pattern_dict[x]) :
                    flag = 1
                    break
            if flag == 0:
                return True
    return False
print(find_permutation('aaacb', 'abc'))
