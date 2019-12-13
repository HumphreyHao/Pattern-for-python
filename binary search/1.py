def binary_search(arr, key):
    left,right = 0,len(arr)-1
    if arr[left]<arr[right]:
        while left<=right:
            mid = left+(right-left)//2
            if arr[mid]<key:
                left=mid+1
            elif arr[mid]>key:
                right =mid-1
            else:
                return mid
    else:
        while left<=right:
            mid = left+(right-left)//2
            if arr[mid]>key:
                left=mid+1
            elif arr[mid]<key:
                right =mid-1
            else:
                return mid
    return -1
        

def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search([10, 6, 4], 10))
  print(binary_search([10, 6, 4], 4))
main()