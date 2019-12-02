import sys
def triplet_sum_close_to_target(arr, target_sum):
    #varible to save the subject,and update the res
    subject = sys.maxsize
    sum = sys.maxsize
    #in the same level, should avoid the repeat
    arr.sort()
    for i in range(len(arr)-3):
        left,right=i+1,len(arr)-1
        while left<right:
            target = arr[left]+arr[right]+arr[i]
            if target_sum>target:
                left+=1
                if abs(target_sum-target)<=subject:
                    subject = target_sum-target
                    sum = min(sum,target)
            elif target_sum<target:
                right-=1
                if abs(target_sum-target)<=subject:
                    subject = abs(target_sum-target)
                    sum = min(sum,target)
            else:
                return 0
    return sum