#level traversal
from collections import deque

class TreeNode:
    def _init_(self,val):
        self.val = val
        self.left,self.right = None,None

def traverse(root,key):
    #use a count save this level
    #valid input
    #care queue is deque so popleft or popright
    result =[]
    queue =deque()
    queue.append(root)
    pre =None
    while len(queue)!=0:
        count = 0
        size = len(queue)
        while(count<size):
            tmp = queue.popleft()
            if pre.val == key:
                return tmp
            pre = tmp
            if tmp.left!= None:
                queue.append(tmp.left)
            if tmp.right!=None:
                queue.append(tmp.right)
            count+=1
    return pre