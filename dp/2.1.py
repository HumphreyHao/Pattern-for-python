def can_partition(num):
    s = sum(num)

  # if 's' is a an odd number, we can't have two subsets with same total
    if s % 2 != 0:
        return False

    # we are trying to find a subset of given numbers that has a total sum of 's/2'.
    s = int(s / 2)
    
    n =len(num)
    dp = [[-1 for x in range(s+1)] for y in range(n)]
    
    #initialize
    for i in range(n):
        #sum ==0 is true
        dp[i][0]=1
    dp[0][num[i]]=1
    for i in range(1,n):
        for j in range(1,s+1):
            if j-num[i]<0:
                dp[i][j]=-1
            else:
                if dp[i-1][j] ==1 or dp[i-1][j-num[i]]==1:
                    dp[i][j]=1
    return dp[n-1][s]==1

def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
    
        