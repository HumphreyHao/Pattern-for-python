#divide and concur
def find_single_numbers(nums):
    left = nums[:len(nums)//2]
    right = nums[len(nums)//2:]
    left_res = find_single_number(left)
    right_res =find_single_number(right)
    if left_res !=0 and right_res!=0:
        return [left_res,right_res]
    else:
        if left_res ==0:
            return find_single_numbers[right]
        else:
            return find_single_numbers[left]

def find_single_number(arr):
    x =arr[0]
    for i in range(1,len(arr)):
        x^=arr[i]
    return x
def main():
  print('Single numbers are:' +
        str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
  print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))

main()