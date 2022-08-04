"""
Compression - Charecter Sequence Tree
"""

# Imports
import os
from .Utils import *

# Main Classes
class Tree:
    def __init__(self, root=None):
        self.root = root

class TreeNode:
    def __init__(self, value, height):
        self.value = value
        self.height = height
        self.children = {}

# Main Functions
def CharSeqTree_GenerateCharSeqTree(data_bytes, groupLength=1, maxTreeHeight=4):
    '''
    CharSeqTree - Generate a character sequence tree from the given data
    '''
    # Init Tree
    root = TreeNode("Start", 0)
    csTree = Tree(root)
    curHeight = 1
    # Add data to tree
    for i in range(0, len(data_bytes), groupLength*maxTreeHeight):
        rindex = groupLength*maxTreeHeight
        if i + groupLength*maxTreeHeight >= len(data_bytes):
            rindex = len(data_bytes) - i
        curNode = csTree.root
        curHeight = 1
        for j in range(0, rindex, groupLength):
            index = i + j + groupLength
            if i + j + groupLength - 1 >= len(data_bytes):
                index = len(data_bytes)
            curNode.children[data_bytes[i+j:index].decode('utf8')] = TreeNode(data_bytes[i+j:index].decode('utf8'), curHeight)
            curNode = curNode.children[data_bytes[i+j:index].decode('utf8')]
            curHeight += 1
        
    return csTree

def CharSeqTree_Compress(filepath=None, data=None, groupLength=1, maxTreeHeight=4, countFormat='dec'):
    '''
    CharSeqTree - Compress data using a character sequence tree
    '''
    # Get data bytes
    if filepath is not None:
        data_bytes = GetBytesFromFile(filepath)
    elif data is not None:
        data_bytes = bytearray(data, encoding="utf8")
    # Generate tree
    csTree = CharSeqTree_GenerateCharSeqTree(data_bytes, groupLength=groupLength, maxTreeHeight=maxTreeHeight)
    
    return csTree

def PrintCharSeqTree(csTreeNode):
    '''
    CharSeqTree - Print the given character sequence tree
    '''
    print(csTreeNode.height, csTreeNode.value)
    for ck in csTreeNode.children.keys():
        PrintCharSeqTree(csTreeNode.children[ck])

# RunCode
# # Params
# data = "FASVHLHLSDAJFHKFSHJBKDKJDIFEHUSKABJNLA:SAFDHLJKNSL:WERQEHLDJKS"
# # Params
# # Compress
# print(len(bytearray(data, encoding='utf8')), bytearray(data, encoding='utf8'))
# compdata = CharSeqTree_Compress(data=data, groupLength=1, maxTreeHeight=10)
# PrintCharSeqTree(compdata.root)