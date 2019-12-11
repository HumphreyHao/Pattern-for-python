#add two longest path+1，check each node for the maximal
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
        diameter = left+right+1
        self.treeDiameter=max(self.treeDiameter,diameter)
        return max(left,right)+1

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    print("Tree Diameter: " + str(find_diameter(root)))
main()
      
      
      
      