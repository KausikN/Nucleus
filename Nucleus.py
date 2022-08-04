"""
Nucleus

Compression
 - Data Stages
    - Input Data
        - dtype: str
    - Intermediate Compressed Data
        - dtype: dict
        - form: 
            {
                "process": "compress",
                "algorithm": "<ALGORITHM>",
                "params": {},
                "data": <ANY>
            }
    - Output Compressed Data
        - dtype: str
 - Functions
    - "compress": Input Data -> Intermediate Compressed Data
    - "compress_encode": Intermediate Compressed Data -> Output Compressed Data
    - "decompress": Intermediate Decompressed Data -> Input Data
    - "decompress_decode": Output Compressed Data -> Intermediate Compressed Data
"""

# Imports
from Algos import CharSeqTree, RunnerLength

# Main Vars
COMPRESSION_FUNCS = {
    "Runner Length": RunnerLength.RUNNERLENGTH_COMPRESSION_FUNCS
}

# Main Functions