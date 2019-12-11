#dfs
class TreeNode:
    def __init__(self,val,left,right):
        super().__init__()
        self.val = val
        self.left = left
        self.right =right

def has_path(root, sum):
    if root == None:
        if sum ==0:
            return True
        else:
            return False
    if root.val>sum:
        return False
    return has_path(root.left,sum - root.val) or has_path(root.right,sum -root.val)
    