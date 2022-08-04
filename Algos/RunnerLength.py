"""
Compression - Runner Length
"""

# Imports
import os
import json

from .Utils import *

# Main Functions
def RunnerLength_Compress(
    data, 
    group_length=1,
    **params
    ):
    '''
    RunnerLength - Runner Length Compression
    Converts Input Data into Intermediate Compressed Data
    '''
    # Init
    CompressedData = {
        "process": "compress",
        "algorithm": "Runner Length",
        "params": {
            "group_length": group_length
        },
        "data": {
            "unique_groups": [],
            "data_groups": []
        }
    }
    data = list(data)
    if len(data) < group_length: group_length = len(data)
    # Compress Data
    curGroup = None
    curCount = 0
    for i in range(0, len(data), group_length):
        s = i
        e = min(i+group_length, len(data))
        group = data[s:e]
        if curGroup is None and e != len(data):
            curGroup = group
            curCount = 1
        elif "".join(curGroup) == "".join(group) and e != len(data):
            curCount += 1
        else:
            groupIndex = -1
            if "".join(curGroup) not in CompressedData["data"]["unique_groups"]:
                CompressedData["data"]["unique_groups"].append("".join(curGroup))
                groupIndex = len(CompressedData["data"]["unique_groups"]) - 1
            else:
                groupIndex = CompressedData["data"]["unique_groups"].index("".join(curGroup))
            CompressedData["data"]["data_groups"].append({"group": groupIndex, "count": curCount})
            curGroup = group
            curCount = 1

    return CompressedData

def RunnerLength_CompressEncode(CompressedData, **params):
    '''
    RunnerLength - Runner Length Compression
    Converts Intermediate Compressed Data to Output Compressed Data
    '''
    # Init
    OutputData = ""
    OutputDict = {
        "process": CompressedData["process"],
        "algorithm": CompressedData["algorithm"],
        "params": CompressedData["params"],
        "data": {
            "unique_groups": CompressedData["data"]["unique_groups"],
            "data_groups": []
        }
    }
    # Encode Data
    for d in CompressedData["data"]["data_groups"]:
        OutputDict["data"]["data_groups"].append([d["group"], d["count"]])
    OutputData = json.dumps(OutputDict)

    return OutputData

def RunnerLength_Decompress(CompressedData, **params):
    '''
    RunnerLength - Runner Length Compression
    Converts Intermediate Compressed Data into Input Data
    '''
    # Init
    data = ""
    if CompressedData["process"] != "compress" or CompressedData["algorithm"] != "Runner Length": return None
    for k in ["group_length"]:
        if k not in CompressedData["params"]: return None
    # Decompress Data
    for d in CompressedData["data"]["data_groups"]:
        data += CompressedData["data"]["unique_groups"][d["group"]] * d["count"]
    
    return data

def RunnerLength_DecompressDecode(OutputData, **params):
    '''
    RunnerLength - Runner Length Compression
    Converts Output Compressed Data into Intermediate Compressed Data
    '''
    # Init
    OutputDict = json.loads(OutputData)
    CompressedData = {
        "process": OutputDict["process"],
        "algorithm": OutputDict["algorithm"],
        "params": OutputDict["params"],
        "data": {
            "unique_groups": OutputDict["data"]["unique_groups"],
            "data_groups": []
        }
    }
    if CompressedData["process"] != "compress" or CompressedData["algorithm"] != "Runner Length": return None
    # Decode Data
    for d in OutputDict["data"]["data_groups"]:
        CompressedData["data"]["data_groups"].append({"group": d[0], "count": d[1]})
    
    return CompressedData

# Main Vars
RUNNERLENGTH_COMPRESSION_FUNCS = {
    "compress": {
        "func": RunnerLength_Compress,
        "params": {
            "group_length": 1
        }
    },
    "compress_encode": {
        "func": RunnerLength_CompressEncode,
        "params": {}
    },
    "decompress": {
        "func": RunnerLength_Decompress,
        "params": {}
    },
    "decompress_decode": {
        "func": RunnerLength_DecompressDecode,
        "params": {}
    }
}