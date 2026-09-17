# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pQueue = deque([p])
        qQueue = deque([q])

        while pQueue:
            node1 = pQueue.popleft()
            node2 = qQueue.popleft()

            if (node1 is None and node2 is not None) or (node2 is None and node1 is not None):
                return False

            if node1 is None and node2 is None:
                return True

            if node1.val != node2.val:
                return False
            
            if node1.left or node2.left:
                pQueue.append(node1.left)
                qQueue.append(node2.left)

            if node1.right or node2.right:
                pQueue.append(node1.right)
                qQueue.append(node2.right)

        return True