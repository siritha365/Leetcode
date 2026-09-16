# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if root == None:
            return []

        q = collections.deque()
        q.append(root)

        while q:
            level = []

            for i in range(len(q)):
                node = q.popleft()

                level.append(node.val)

                if node.left != None:
                    q.append(node.left)

                if node.right != None:
                    q.append(node.right)

            res.append(max(level))

        return res      
        
        