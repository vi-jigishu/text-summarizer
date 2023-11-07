#the functions tha will be used frequently in our code is written here in util(commin.py) so that we dont have to write things again and again
import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensurepip import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any  


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read a YAML file and return

    Args:
        path_to_yaml (str): path like input
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    
    Returns:
        ConfigBox: ConfigBox type
    """
    
    try:
        with open(path_to_yaml) as yaml_file:
            content= yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
            
