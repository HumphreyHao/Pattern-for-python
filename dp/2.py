def can_partition(num):
    '''
    try to find a subarr to get the sum =1/2 * all sum
    '''
    allSum=sum(num)
    if allSum%2 !=0:
        return False
    else:
        dp=[[-1 for x in range(int(allSum/2)+1)]for y in range(len(num))]
        return True if helper(dp,num,allSum//2,0)==1 else False
def helper(dp,num,cur,start):
    if cur ==0:
        return 1
    if start >=len(num) or cur<0:
        return 0
    if dp[start][cur]==-1:
        if helper(dp,num,cur-num[start],start+1)==1:
            dp[start][cur]=1
            return 1
        dp[start][cur]=helper(dp,num,cur,start+1)
    return dp[start][cur]

def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()