import os 
from box.exceptions import BoxValueError
import yaml
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox 
from typing import Any
import base64
from pathlib import Path
from srcTrackVision import logger
from yaml.loader import SafeLoader

# @ensure_annotations
def read_yaml(path: str) -> ConfigBox:
    """Read a yaml file and return a ConfigBox object
    
    Raises : 
        ValueError: If yaml file is empty
        e : empty file 


    Returns:
         ConfigBox: ConfigBox object
    """

    try:
        with open(path) as yaml_file:
            content = yaml.load(yaml_file , Loader = SafeLoader)
            logger.info(f'yaml file {path} loaded successfully')
            return ConfigBox(content)
        
    except BoxValueError :
        raise ValueError(f'yaml file {path} is empty')
    
    except Exception as e : 
        raise e 
    



@ensure_annotations
def create_directories(path: list, verbose=True):
    """
    Create list of directories

    Args:
        path (list): List of directories to be created
        verbose (bool, optional): Ignore if multiple directories are being created. Defaults to True.
    """
    for p in path:
        os.makedirs(p, exist_ok=True)
        if verbose:
            logger.info(f'Created directory at: {p}')




@ensure_annotations
def save_json(path : str, data : dict):
    """save json data
    
    Args : 
        path (str) : path to save json file
        data (dict) : json data to be saved
    """

    with open(path , 'w') as json_file:
        json.dump(data , json_file , indent=4)

    logger.info(f'json file {path} saved successfully')


@ensure_annotations
def get_size(path : Path) -> str : 
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~{size_in_kb} KB"





