#check each substr, if it can be deleted for all words, add it to the result
##better way：like check the K char, use a set to save the words have been seen, and update the win_set
def find_word_concatenation(str, words):
    result_indices = []
    left,right = 0,0
    length=0
    for i in words:
        length+=len(i)
    for right in range(len(str)):
        if right<length-1:
            continue
        if check(str[left:right+1],words) ==1:
            result_indices.append(left)
        left+=1
    return result_indices
def check(str1:str,words):
    for i in words:
        if i not in str1:
            return 0
        else:
            str1=str1.replace(i,'',1)
    if len(str1) == 0:
        return 1
    return 0
find_word_concatenation('catfoxcat', ['cat', 'fox'])