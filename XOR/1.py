def find_single_number(arr):
    x =arr[0]
    for i in range(1,len(arr)):
        x^=arr[i]
    return x

def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))

main()