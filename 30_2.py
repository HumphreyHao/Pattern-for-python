#better way, read from end to head
def backspace_compare(str1, str2):
    res1 = read(str1)
    res2 = read(str2)
    return res1== res2

def read(str1):
    res1 = []
    for i in str1:
        if i !='#':
            res1.append(i)
        else:
            res1.pop(len(res1)-1)
    return res1
    
