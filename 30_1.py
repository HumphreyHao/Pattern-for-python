#recursively solve this problem
#avoid repeat!
def search_quadruplets(arr, target):
    #sort the array
    arr.sort()
    for i in range(len(arr)-1):
        tmp = []
