#same as five, but the height become the sum of one side of each node
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeDiameter:
    def __init__(self):
        super().__init__()
        self.treeDiameter =0
    def find_diameter(self,root):
        self.cal(root)
        return self.treeDiameter
    def cal(self,root):
        if root ==None:
            return 0
        left=self.cal(root.left)
        right = self.cal(root.right)
        diameter = left+right+root.val
        self.treeDiameter=max(self.treeDiameter,diameter)
        return max(left,right)+root.val

def main():
  treeDiameter=TreeDiameter()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)

  print("Maximum Path Sum: " + str(treeDiameter.find_diameter(root)))
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(3)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  print("Maximum Path Sum: " + str(treeDiameter.find_diameter(root)))
  root = TreeNode(-1)
  root.left = TreeNode(-3)
  print("Maximum Path Sum: " + str(treeDiameter.find_diameter(root)))


main()
