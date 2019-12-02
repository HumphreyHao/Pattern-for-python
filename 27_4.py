def search_triplets(arr):
    #in the same level, should avoid the repeat
    triplets = []
    arr.sort()
    for i in range(len(arr)-3):
        left,right=i+1,len(arr)-1
        while left<right:
            target = arr[left]+arr[right]
            if target<-arr[i]:
                left+=1
            elif target>-arr[i]:
                right-=1
            else:
                tmp =[arr[i],arr[left],arr[right]]
                right-=1
                if tmp not in triplets:
                    triplets.append(tmp)
    return triplets

    