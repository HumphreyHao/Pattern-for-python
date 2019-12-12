#cut n as two parts, and recursively solve
#avoid the repeat
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_unique_trees(n):
    
    if n==1 or n <=0:
        return 1
    if n==2:
        return 2
    count=0
    for i in range(n):
        left = find_unique_trees(i)
        right = find_unique_trees(n-i-1)
        count+=left*right
    return count
        


def main():
  print(find_unique_trees(2))


main()