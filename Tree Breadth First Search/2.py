from collections import deque
def traverse(root):
    #use a count save this level
    #valid input
    #care queue is deque so popleft or popright
    #list can also append left
    #deque[0] is peek()
    #deque.pop is from the end, pop left is from the right
    #use deque 辅助dfs可以不用写递归，把下一层的压进去即可。
    result =[]
    queue =deque()
    queue.append(root)
    while len(queue)!=0:
        count = 0
        size = len(queue)
        while(count<size):
            tmp = queue.popleft()
            result.append(tmp.val)
            if tmp.left!= None:
                queue.append(tmp.left)
            if tmp.right!=None:
                queue.append(tmp.right)
            count+=1
    return result.reverse()