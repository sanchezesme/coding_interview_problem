# Definition for a binary tree node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        pass


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        pass




def run():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    #assert deserialize(serialize(node)).left.left.val == 'left.left'
    codec = Codec()
    print(codec.serialize(node))

if __name__ == '__main__':
    run()