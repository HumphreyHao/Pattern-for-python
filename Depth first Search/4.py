class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def count_paths(root, S):
    return helper(root,S,[])

def helper(root,S,path):
    if root is None:
        return 0
    path.append(root.val)
    pathCount, pathSum=0,0
    #from end to start, try to see if any root has the sum
    for i in range(len(path)-1,-1,-1):
        pathSum +=path[i]
        if pathSum ==S:
            pathCount+=1
    pathCount+=helper(root.left,S,path)
    pathCount+=helper(root.right,S,path)
    del path[-1]
    
    return pathCount
    
    
    
    
def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()