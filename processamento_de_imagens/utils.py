import os 

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

def in_path(filename: str):
    '''
    # Description

    Gets the relative path to `filename` that must be at `input`
    folder

    ## Parameters
    `- filename:str` the name of the target file. This file must be
    located at `INPUT_FOLDER`;
    `- return:str` the relative path to `filename`.
    '''

    return os.path.join(INPUT_FOLDER, filename)


def out_path(filename: str):
    '''
    # Description

    Gets the relative path to `filename` that must be at `output`
    folder

    ## Parameters
    `- filename:str` the name of the target file. This file must be
    located at `OUTPUT_FOLDER`;
    `- return:str` the relative path to `filename`.
    '''

    return os.path.join(OUTPUT_FOLDER, filename)