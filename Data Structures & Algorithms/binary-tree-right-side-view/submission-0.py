# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue, results = [], []
        if root:
            queue.append(root)
        while queue:
            curr_len, curr_list = len(queue), []
            for x in range(curr_len):
                curr_list.append(queue[0].val)
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                del queue[0]
            results.append(curr_list[-1])
        return results