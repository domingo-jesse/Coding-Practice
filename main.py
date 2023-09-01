#Daily programing Practice 


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Post0order tree Transerval
#Left,right, visit

lass Solution(object):
      def postorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res
    
      def helper(self, root, res):
            if root:
                self.helper(root.left, res)
                self.helper(root.right, res)
                res.append(root.val)


# Pre-order tree Transveral
#visit, left, right

class Solution(object):
      def preorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res
    
      def helper(self, root, res):
        if root:
          res.append(root.val)
          self.helper(root.left, res)
          self.helper(root.right, res)
# In-Order tree Transversl 
#left, visit, right 

class Solution(object):
      def inorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res
    
      def helper(self, root, res):
            if root:
                self.helper(root.left, res)
                res.append(root.val)
                self.helper(root.right, res)

 


#DPS 
def dfs(graph, node):
    visited = []
    stack = []

    visited.append(node)
    stack.append(node) 

    while stack:
        s = stack.pop()
        print(s, end = " ")

        # reverse iterate through edge list so results match recursive version
        for n in reversed(graph[s]):
            if n not in visited:
                visited.append(n)
                stack.append(n)

def main():
    dfs(graph, 'A')

main()
#BPS

def bfs(graph, node):
    visited = []
    # the video has queue as an array. I changed this to deque because popping the first element is O(1) instead of O(n).
    # see this link for more: https://wiki.python.org/moin/TimeComplexity.
    queue = deque()

    visited.append(node)
    queue.append(node)

    while queue:
        # popleft is O(1). for an array, pop(0) is O(n). hence the change to deque from array.
        s = queue.popleft()
        print(s, end = " ")

        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

def main():
    bfs(graph, 'A')

main()



#linear search

#binary Search 



#Sorting algos
  #Bubble Sort
  #Insertion Sort
  #Selection Sort
  #Quick Sort
  #Heap sort
  #merge sort 

#

# hashing 
# insert into a linked list 
#two sum (has tables)

