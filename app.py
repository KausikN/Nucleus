"""
Stream lit GUI for hosting Nucleus
"""

# Imports
import os
import streamlit as st
import json

import Nucleus

# Main Vars
config = json.load(open("./StreamLitGUI/UIConfig.json", "r"))

# Main Functions
def main():
    # Create Sidebar
    selected_box = st.sidebar.selectbox(
    "Choose one of the following",
        tuple(
            [config["PROJECT_NAME"]] + 
            config["PROJECT_MODES"]
        )
    )
    
    if selected_box == config["PROJECT_NAME"]:
        HomePage()
    else:
        correspondingFuncName = selected_box.replace(" ", "_").lower()
        if correspondingFuncName in globals().keys():
            globals()[correspondingFuncName]()
 

def HomePage():
    st.title(config["PROJECT_NAME"])
    st.markdown("Github Repo: " + "[" + config["PROJECT_LINK"] + "](" + config["PROJECT_LINK"] + ")")
    st.markdown(config["PROJECT_DESC"])

    # st.write(open(config["PROJECT_README"], "r").read())

#############################################################################################################################
# Repo Based Vars
CACHE_PATH = "StreamLitGUI/CacheData/Cache.json"
DEFAULT_PATHS = {
    "temp": "StreamLitGUI/TempData/",
    "file": {
        "text": "Data/InputFiles/test.txt"
    }
}

# Util Vars
CACHE = {}

# Util Functions
def LoadCache():
    global CACHE
    CACHE = json.load(open(CACHE_PATH, "r"))

def SaveCache():
    global CACHE
    json.dump(CACHE, open(CACHE_PATH, "w"), indent=4)

# Algo Functions
def UI_LoadAlgo_Compression():
    '''
    Load Compression Algorithm
    '''
    USERINPUT_Algo = st.selectbox("Compression Algo", list(Nucleus.COMPRESSION_FUNCS.keys()))
    USERINPUT_CompressMode = st.sidebar.selectbox("Mode", ["Compress", "Decompress"])
    if USERINPUT_CompressMode == "Compress":
        USERINPUT_AlgoParams = {}
        cols = st.columns(2)
        USERINPUT_AlgoParams["compress"] = json.loads(cols[0].text_area(
            "Compression Params", 
            value=json.dumps(Nucleus.COMPRESSION_FUNCS[USERINPUT_Algo]["compress"]["params"], indent=4),
            height=250
        ))
        cols[0].write(USERINPUT_AlgoParams["compress"])
        USERINPUT_AlgoParams["compress_encode"] = json.loads(cols[1].text_area(
            "Compression Encoding Params", 
            value=json.dumps(Nucleus.COMPRESSION_FUNCS[USERINPUT_Algo]["compress_encode"]["params"], indent=4),
            height=250
        ))
        cols[1].write(USERINPUT_AlgoParams["compress_encode"])
        USERINPUT_Algo = {
            "mode": USERINPUT_CompressMode,
            "funcs": [
                {
                    "func": Nucleus.COMPRESSION_FUNCS[USERINPUT_Algo]["compress"]["func"],
                    "params": USERINPUT_AlgoParams["compress"]
                },
                {
                    "func": Nucleus.COMPRESSION_FUNCS[USERINPUT_Algo]["compress_encode"]["func"],
                    "params": USERINPUT_AlgoParams["compress_encode"]
                }
            ]
        }
    else:
        USERINPUT_AlgoParams = {}
        cols = st.columns(2)
        USERINPUT_AlgoParams["decompress"] = json.loads(cols[0].text_area(
            "Decompression Params", 
            value=json.dumps(Nucleus.COMPRESSION_FUNCS[USERINPUT_Algo]["decompress"]["params"], indent=4),
            height=250
        ))
        cols[0].write(USERINPUT_AlgoParams["decompress"])
        USERINPUT_AlgoParams["decompress_decode"] = json.loads(cols[1].text_area(
            "Decompression Decoding Params", 
            value=json.dumps(Nucleus.COMPRESSION_FUNCS[USERINPUT_Algo]["decompress_decode"]["params"], indent=4),
            height=250
        ))
        cols[1].write(USERINPUT_AlgoParams["decompress_decode"])
        USERINPUT_Algo = {
            "mode": USERINPUT_CompressMode,
            "funcs": [
                {
                    "func": Nucleus.COMPRESSION_FUNCS[USERINPUT_Algo]["decompress_decode"]["func"],
                    "params": USERINPUT_AlgoParams["decompress_decode"]
                },
                {
                    "func": Nucleus.COMPRESSION_FUNCS[USERINPUT_Algo]["decompress"]["func"],
                    "params": USERINPUT_AlgoParams["decompress"]
                }
            ]
        }

    return USERINPUT_Algo

# UI Functions
def UI_LoadData_Text():
    '''
    Load Text Data
    '''
    # Load Text
    USERINPUT_InputMode = st.selectbox("Input Mode", ["Enter Text", "Upload File"])
    if USERINPUT_InputMode == "Enter Text":
        USERINPUT_Input = st.text_area("Enter Text", value="112233")
    else:
        USERINPUT_Input = st.file_uploader("Upload File")
        if USERINPUT_Input is None: USERINPUT_Input = open(DEFAULT_PATHS["file"]["text"], "rb")
        USERINPUT_Input = str(USERINPUT_Input.read().decode("utf-8"))

    return USERINPUT_Input

# Repo Based Functions
def compress_algos():
    # Title
    st.header("Compression Algorithms")

    # Prereq Loaders

    # Load Inputs
    USERINPUT_Text = UI_LoadData_Text()
    USERINPUT_AlgoData = UI_LoadAlgo_Compression()

    # Process Inputs
    if st.button(USERINPUT_AlgoData["mode"]):
        # Run Algo Funcs
        RunData = USERINPUT_Text
        for f in USERINPUT_AlgoData["funcs"]:
            RunData = f["func"](RunData, **f["params"])
        USERINPUT_Output = RunData
        # Display Outputs
        st.markdown("# Output")
        st.text_area("Output Data", USERINPUT_Output)
        # Visualise
        st.markdown("# Visualisations")
        st.markdown("## Input")
        VisData_Input = {
            "length": len(USERINPUT_Text),
            "size (bytes)": len(USERINPUT_Text)
        }
        st.write(VisData_Input)
        st.markdown("## Output")
        VisData_Output = {
            "length": len(USERINPUT_Output),
            "size (bytes)": len(USERINPUT_Output)
        }
        st.write(VisData_Output)
        
    
#############################################################################################################################
# Driver Code
if __name__ == "__main__":
    main()