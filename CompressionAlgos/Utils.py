'''
Summary
Utils for Compression Algos
'''

import os

def GetBytesFromFile(filepath):
    return bytearray(open(filepath, 'rb').read())