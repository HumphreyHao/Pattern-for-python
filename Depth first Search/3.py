#find all the paths
#add
class TreeNode:
    def __init__(self,val,left=None,right=None):
        super().__init__()
        self.val = val
        self.left = left
        self.right =right

def find_sum_of_path_numbers(root):
    allPaths=[]
    dfs(root,allPaths,[])
    res =[]
    for path in allPaths:
        str_sum =""
        for i in path:
            str_sum+=str(i.val)
        res.append(int(str_sum))
    return sum(res)

def dfs(root,allPaths,nowPath):
    if root == None:
        return
    nowPath.append(root)
    if root.left == None and root.right == None:
        allPaths.append(list(nowPath))
    else:
        dfs(root.left,allPaths,nowPath)
        dfs(root.right,allPaths,nowPath)
    nowPath.pop()

def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()