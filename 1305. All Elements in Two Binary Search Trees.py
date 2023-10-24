# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
            if root1 is None:
                result = []
            else:
                result = tree_to_array(root1)
            if root2 is None:
                result += []
            else:
                result += tree_to_array(root2)
            sorted_result = sorted(result)
            return sorted_result

def tree_to_array(root):
    if root is None:
        return []

    result = []

    # In-order traversal (change the order for other types of traversal)
    result += tree_to_array(root.left)
    result.append(root.val)
    result += tree_to_array(root.right)

    return result
