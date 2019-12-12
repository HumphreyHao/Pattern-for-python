#exchange with each position, then find all the sublist
def find_permutations(nums):
    lists=[]
    list1=[]
    helper(nums,list1,lists)
    return lists
def helper(nums,list1,lists):
    if len(nums)==0:
        lists.append(list(list1))
        return
    for i in nums:
        list1.append(i)
        tmp =list(nums)
        tmp.remove(i)
        helper(tmp,list1,lists)
        del list1[-1]
        
        
        
        

def main():
  print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))
main()