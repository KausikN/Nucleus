'''
Summary
Compression by Charecter Sequence Tree Method
'''
import os
import Utils

# ------- Charecter Sequence Tree -----------------------------------------------------------------------------------------------------

def CharSeqTree_Compress(filepath=None, data=None, groupLength=1, maxTreeHeight=4, countFormat='dec'):
    compressed_bytes = ''
    if not filepath == None:
        data_bytes = Utils.GetBytesFromFile(filepath)
    elif not data == None:
        data_bytes = bytearray(data, encoding='utf8')

    csTree = GenerateCharSeqTree(data_bytes, groupLength=groupLength, maxTreeHeight=maxTreeHeight)
    return csTree



    return bytearray(compressed_bytes, encoding='utf8')

# ------- Charecter Sequence Tree -----------------------------------------------------------------------------------------------------

# Util Functions
def GenerateCharSeqTree(data_bytes, groupLength=1, maxTreeHeight=4):
    # Init Tree
    root = TreeNode('Start', 0)
    csTree = Tree(root)
    curHeight = 1

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


def PrintCharSeqTree(csTreeNode):
    print(csTreeNode.height, csTreeNode.value)
    for ck in csTreeNode.children.keys():
        PrintCharSeqTree(csTreeNode.children[ck])



# Tree Classes
class Tree:
    def __init__(self, root=None):
        self.root = root
        

class TreeNode:
    def __init__(self, value, height):
        self.value = value
        self.height = height
        self.children = {}


# Driver Code
data = "FASVHLHLSDAJFHKFSHJBKDKJDIFEHUSKABJNLA:SAFDHLJKNSL:WERQEHLDJKS"
print(len(bytearray(data, encoding='utf8')), bytearray(data, encoding='utf8'))
compdata = CharSeqTree_Compress(data=data, groupLength=1, maxTreeHeight=10)
PrintCharSeqTree(compdata.root)
# filepath = 'CompressionAlgos/testfile.txt'
# compdata = RunnerLength_Compress(filepath=filepath, groupLength=3, countFormat='dec')
# print(len(compdata), compdata)
# decompdata = RunnerLength_Decompress(data=compdata, countFormat='dec')
# print(len(decompdata), decompdata)
