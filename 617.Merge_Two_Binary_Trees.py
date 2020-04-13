# 递归
# 相同位置上的两个结点都不存在的话，直接返回即可
# 如果 t1 存在，t2 不存在，就以 t1 的结点值建立一个新结点，然后分别对 t1 的左右子结点和空结点调用递归函数
# 如果 t1 不存在，t2 存在，就以 t2 的结点值建立一个新结点，然后分别对 t2 的左右子结点和空结点调用递归函数
# 如果 t1 和 t2 都存在，就以 t1 和 t2 的结点值之和建立一个新结点，然后分别对 t1 的左右子结点和 t2 的左右子结点调用递归函数


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            newT = TreeNode(t1.val +  t2.val)
            newT.left = self.mergeTrees(t1.left, t2.left)
            newT.right = self.mergeTrees(t1.right, t2.right)
            return newT
        else:
            return t1 or t2


def create_tree(lis):
    [ t for i  in lis ]
    t = TreeNode()
    t1.left = TreeNode(3)
    t1.right = TreeNode(2)
    t1.left.left = 5
    load_tree(t1)


if __name__ == "__main__":


    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.right = TreeNode(3)
    t2.left.right = 4
    t2.right.right = 7
    load_tree(t2)

    # s = Solution()
    # result = s.mergeTrees(t1,t2)



