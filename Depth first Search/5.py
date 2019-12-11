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


      
      
      
      