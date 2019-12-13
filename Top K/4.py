def find_k_frequent_numbers(nums, k):
    fre_count={}
    for i in nums:
        if i in fre_count:
            fre_count[i]+=1
        else:
            fre_count[i]=1
    mostpopular=[(fre_count[name],name) for name in fre_count]
    mostpopular.sort()
    mostpopular.reverse()
    res=[]
    for i in range(len(mostpopular)):
        if i<k:
            count,name =mostpopular[i]
            res.append(name)
    return res

        


def main():

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()