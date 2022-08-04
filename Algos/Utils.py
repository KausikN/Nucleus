"""
Utils
"""

# Imorts
import os

# Main Functions
def GetBytesFromFile(filepath):
    '''
    Utils - Get the bytes from the given file
    '''
    return bytearray(open(filepath, 'rb').read())