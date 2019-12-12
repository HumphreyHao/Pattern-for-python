#generate all subset
def find_subsets(nums):
    res=[[]]
    left,right =0,0
    for right in range(len(nums)):
        tmp=nums[left:right+1]
        if tmp not in res:
            res.append(tmp)
    for left in range(len(nums)):
        tmp =nums[left:right+1]
        if tmp not in res:
            res.append(tmp)
    return res

def main():
    
  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
    
    