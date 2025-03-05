import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        arr_nodes = [root] # Act as a queue
        arr_data = []
        
        while len(arr_nodes) > 0:
            current_node = arr_nodes.pop(0)
            arr_data.append(current_node.data)
            
            if current_node.left is not None:
                arr_nodes.append(current_node.left)
            if current_node.right is not None:
                arr_nodes.append(current_node.right)
        
        print(*arr_data)
            
        

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
