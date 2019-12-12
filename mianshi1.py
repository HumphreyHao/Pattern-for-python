def find_duplicates(arr1, arr2):
    #for each  element in arr2
    #binary search it in arr1
    res =[]
    for i in arr2:
        if binarySearch(i,arr1):
            res.append(i)
    return res

def binarySearch(i,arr1):
    left,right=0,len(arr1)-1
    while left<=right:
        mid = left+(right-left)//2
        if arr1[mid]==i:
            return True
        elif arr1[mid]<i:
            left = mid+1
        else:
            right=mid-1
    return False
def main():
    print(find_duplicates([1,2,3,5,6,7],[3,6,7,8,20]))
main()