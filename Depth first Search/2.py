#dfs and deep copy, new =list() is similar with new ...
class TreeNode:
    def __init__(self,val,left=None,right=None):
        super().__init__()
        self.val = val
        self.left = left
        self.right =right

def find_paths(root, sum):
    allPaths =[]
    nowPath = []
    dfs(root,sum,allPaths,nowPath)
    return len(allPaths)

def dfs(root,sum,allPaths,nowPath):
    if root == None:
        return
    if root.val>sum:
        return
    nowPath.append(root)
    if root.val == sum and root.left == None and root.right == None:
        allPaths.append(list(nowPath))
    else:
        dfs(root.left,sum-root.val,allPaths,nowPath)
        dfs(root.right,sum-root.val,allPaths,nowPath)
    nowPath.pop()

def main():
    
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  sum = 23
  print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))


main()
    
        
    

